from PySide6.QtCore import QThread, QUrl, QEventLoop, Signal, QFile, QIODevice
from PySide6.QtGui import Qt, QTextCursor
from PySide6.QtWidgets import (QMainWindow, QApplication,
                               QButtonGroup, QCheckBox,
                               QTableWidgetItem, QMessageBox,
                               QFileDialog)
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import os
import time
import sys

from mainWin_ui import Ui_MainWindow

OK = 1
ERROR = 0


class CrawlThread(QThread):
    """
    document: 线程级的下载器
    """
    finish_signal = Signal()    # 下载完成时发送的信号

    def __init__(self, parent=None):
        super(CrawlThread, self).__init__(parent)
        self.window = parent
        self.flag = True    # 下载停止的标志位
        self.network_manager = QNetworkAccessManager(self)
        self.network_reply = None
        self.current_name = ''

    def run(self):
        """
        document: 视频爬取循环
        :return: None
        """
        self.flag = True
        if self.flag:
            for url in self.window.down_list:
                self.window.ui.progressBar.setValue(0)
                self.crawl_video(url)

        self.current_name = ''
        self.finish_signal.emit()

    def down_video(self, name, url):
        """
        根据获取指定的url的资源
        :param name: str 文件名
        :param url: str 网址
        :return: None
        """
        self.current_name = name
        link = QUrl(url)
        request = QNetworkRequest(link)
        request.setRawHeader(b"Referer", b"https://www.tangdou.com/")
        request.setRawHeader(b"User-Agent", b"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0")
        loop = QEventLoop()

        # 发送请求并等待完成
        self.network_reply = self.network_manager.get(request)
        self.network_reply.downloadProgress.connect(self.update_progress)
        self.network_reply.finished.connect(loop.quit)

        loop.exec_()  # 进入事件循环等待完成

        # 现在网络请求已经完成，可以继续执行其他操作
        self.download_finished()

    def update_progress(self, bytes_received, total_bytes):
        if total_bytes > 0:
            progress_percentage = (bytes_received / total_bytes) * 100
            self.window.ui.progressBar.setValue(progress_percentage)

    def download_finished(self):
        if self.network_reply.error() == QNetworkReply.NoError:
            # 下载完成时的处理代码
            video = self.network_reply.readAll()
            # print(video)
            # 创建QFile对象
            file_path = self.window.g_szDestination + '/' + self.current_name + '.mp4'
            file = QFile(file_path)
            # 打开文件以写入二进制数据

            if file.open(QIODevice.WriteOnly):
                # 将QByteArray写入文件
                file.write(video)
                # 关闭文件
                file.close()
                print(f"Data written to {file_path}")
            else:
                print(f"Failed to open {file_path} for writing")
            # 这里你可以保存数据到文件或者进行其他处理
            print("Download completed")
            self.window.ui.textBrowser_output.append('*** --{}-- 下载成功!***'.format(self.current_name))
            return OK
        else:
            # 处理下载失败的情况
            self.window.ui.textBrowser_output.append('*** ----- 下载失败: {} -----***'.format(
                            self.network_reply.errorString()))
            return ERROR

    def crawl_video(self, url):
        """
        document: 下载入口， 获取指定url的资源信息
        :param url: str 网址
        :return: 状态码[OK, ERROR]
        """
        driver = None
        if self.window.g_szDriveName == "Firefox":
            driver = webdriver.Firefox(service=Service(self.window.g_szDriveDir))
        if self.window.g_szDriveName == "Google":
            driver = webdriver.Chrome(service=Service(self.window.g_szDriveDir))
        if self.window.g_szDriveName == "Edge":
            driver = webdriver.Edge(service=Service(self.window.g_szDriveDir))

        if driver is not None:
            src, name = '', ''     # 接收实际的url， 文件的名字
            driver.get(url)
            driver.minimize_window()
            time.sleep(5)
            try:
                div_video = driver.find_element(By.CLASS_NAME, 'video-waper')
                div_name = driver.find_element(By.CLASS_NAME, 'info')

                src = div_video.find_element(By.TAG_NAME, 'video').get_attribute('src')
                name = div_name.find_element(By.CLASS_NAME, 'title').text.strip().replace(' ', '')
                print(src)

                self.window.ui.textBrowser_output.append('*** --{}-- 正在下载!***'.format(name))
                if name in [file.split('.')[0] for file in os.listdir(self.window.g_szDestination)]:
                    self.window.ui.progressBar.setValue(100)
                    self.window.ui.textBrowser_output.append('*** --{}-- 下载完成!***'.format(name))
                    return OK
                self.down_video(name=name, url=src)
            except NoSuchElementException:
                self.window.ui.textBrowser_output.append('*** --{}-- 当前视频资源失效!***'.format(name))
                return ERROR
            finally:
                driver.close()
        else:
            return ERROR

    def stop(self):
        """
        document: 停止下载
        :return: None
        """
        self.flag = False


class TdWindow(QMainWindow):
    """
    document: 主窗口，提供可视化界面下载视频
    """
    def __init__(self, parent=None):
        super(TdWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.crawl_thread = CrawlThread(self)
        self.button_group = None
        self.g_szDriveName = ''     # 选择的驱动名字
        self.g_szDriveDir = ''      # 驱动所在文件路径
        self.g_szDestination = ''   # 下载视频的保存地址
        self.g_szList = []          # 待下载列表
        self.down_list = []         # 实际下载列表
        self.init_ui()              # 初始化UI
        self.init_signal_and_slot()     # 初始信号与槽函数

    def init_ui(self):
        """
        document: 初始3个单选按钮的状态，由一个QButtonGroup类接收
        :return: None
        """
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.ui.radioButton_firefox)
        self.button_group.addButton(self.ui.radioButton_google)
        self.button_group.addButton(self.ui.radioButton_edge)

    def init_signal_and_slot(self):
        """
        document: 初始信号与槽函数
        :return: None
        """
        self.button_group.buttonClicked.connect(self.get_info)
        self.ui.btn_load_driver.clicked.connect(self.load_driver)  # 加载驱动路径

        self.ui.btn_add.clicked.connect(self.add_url)
        self.ui.btn_browse.clicked.connect(self.load_dir)

        self.ui.checkBox_all.stateChanged.connect(self.change_all_state)  # 全选下载项
        self.ui.btn_cls_table.clicked.connect(self.clean_table)     # 清空表格

        self.ui.btn_download.clicked.connect(self.download_videos)
        self.ui.btn_cls_list.clicked.connect(self.clean_list)

        self.crawl_thread.finish_signal.connect(self.finished)

    def add_url(self):
        """
        document: 添加url，并将其加入待下载队列中
        :return: None
        """
        url = self.ui.lineEdit_url.text().strip()
        if not url:
            return 0
        self.g_szList.append(url)
        self.ui.lineEdit_url.setText('')
        # print(g_szList)
        len_row = len(self.g_szList)
        self.ui.tableWidget_url.clearContents()
        self.ui.tableWidget_url.setRowCount(len_row)
        for i in range(len_row):
            cell = QTableWidgetItem(self.g_szList[i])
            cell.setFlags(cell.flags() ^ Qt.ItemIsEditable)

            check = QCheckBox('')
            # check.setChecked(False)
            check.stateChanged.connect(self.get_state)

            self.ui.tableWidget_url.setItem(i, 0, cell)
            self.ui.tableWidget_url.setCellWidget(i, 1, check)

        self.ui.tableWidget_url.resizeColumnsToContents()

    def clean_list(self):
        """
        document: 清除实际下载队列，待下载队列依旧保留
        :return: None
        """
        len_row = len(self.g_szList)
        for i in range(len_row):
            check = self.ui.tableWidget_url.cellWidget(i, 1)
            if check.isChecked():
                check.setChecked(False)

    def clean_table(self):
        """
        document: 清除待下载队列，所有的url彻底清除
        :return: None
        """
        self.g_szList.clear()
        self.ui.listWidget.clear()
        self.ui.tableWidget_url.clearContents()
        self.ui.tableWidget_url.setRowCount(len(self.g_szList))

    def get_state(self):
        """
        document: 获取待下载队列中url的QCheckButton选中的状态，将选中的加入实际下载队列
        :return: None
        """
        len_row = self.ui.tableWidget_url.rowCount()
        # print(self.ui.tableWidget_url.cellWidget(0, 1))
        self.ui.listWidget.clear()  # 每次变化时，先清空列表，再加载
        for i in range(len_row):
            if self.ui.tableWidget_url.cellWidget(i, 1).isChecked():
                url = self.ui.tableWidget_url.item(i, 0).text().strip()
                self.ui.listWidget.addItem(url)

    def change_all_state(self):
        """
        document: 全选复选框的状态
        :return: None
        """
        len_row = len(self.g_szList)
        # print(self.g_szList)
        state = self.ui.checkBox_all
        for i in range(len_row):
            check = self.ui.tableWidget_url.cellWidget(i, 1)
            if not check.isChecked():
                check.setChecked(True)
        if not state.isChecked():
            for i in range(len_row):
                self.ui.tableWidget_url.cellWidget(i, 1).setChecked(False)

    def download_videos(self):
        """
        document: 下载当前下载队列的url
        :return: None
        """
        if self.ui.btn_download.text().strip() == "开始下载":
            if not self.check_state():
                QMessageBox.warning(self, "警告", "初始化参数错误!", QMessageBox.Ok)
                return ERROR
            len_row = self.ui.listWidget.count()
            if len_row:
                # 添加到下载队列
                for i in range(len_row):
                    self.down_list.append(self.ui.listWidget.item(i).text().strip())
                # print(self.down_list)
                if self.down_list:
                    self.start_crawling()
            else:
                QMessageBox.warning(self, "警告", "下载队列为空!", QMessageBox.Ok)
        else:
            self.down_list.clear()
            self.stop_crawling()

    def check_state(self):
        """
        document: 检查驱动和文件保存路径的状态
        :return:
        """
        if self.g_szDriveName or self.g_szDriveDir or self.g_szDestination:
            return OK
        return ERROR

    def start_crawling(self):
        """
        document: 开始加载下载线程
        :return: None
        """
        self.ui.textBrowser_output.clear()
        self.show_log("***开始下载***")
        self.ui.btn_download.setText("停止下载")

        if not self.crawl_thread.isRunning():
            self.crawl_thread.start()

    def stop_crawling(self):
        """
        document: 停止下载线程
        :return: None
        """
        self.show_log("***正在停止下载***")
        self.ui.btn_download.setText("正在停止...")
        self.ui.btn_download.setEnabled(False)
        self.crawl_thread.stop()

    def finished(self):
        """
        document: 结束下载
        :return: None
        """
        self.show_log("***下载结束***")
        self.ui.btn_download.setText("开始下载")
        self.ui.btn_download.setEnabled(True)
        self.down_list.clear()

    def show_log(self, log):
        """
        document: 输出下载状态日志
        :param log:
        :return:
        """
        self.ui.textBrowser_output.append(log)
        self.ui.textBrowser_output.moveCursor(QTextCursor.End)

    def get_info(self):
        """
        document: 获取选择指定的驱动类型
        :return: None
        """
        sender = self.sender().checkedButton()
        self.g_szDriveName = sender.text()
        # print(self.g_szDriveName)

    def load_driver(self):
        """
        document: 选择指定驱动类型，并加载该驱动文件
        :return: None
        """
        if self.g_szDriveName:
            self.g_szDriveDir = QFileDialog.getOpenFileName(None, "选择驱动文件", "C:\\")[0]
            # print(self.g_szDriveDir)
            if self.g_szDriveDir:
                self.ui.label_driver_dir.setText("驱动位置: " + self.g_szDriveDir)
                # print("选择的驱动器路径为：", self.g_szDriveDir)
        else:
            QMessageBox.warning(self, "警告", "请选择浏览器驱动器", QMessageBox.Ok)

    def load_dir(self):
        """
        document: 加载文件保存路径
        :param self:
        :return:
        """
        self.g_szDestination = QFileDialog.getExistingDirectory(None, "选择保存路径", "C:\\")
        # print(self.g_szDestination)
        if self.g_szDestination:
            self.ui.label_save_dir.setText("保存位置: " + self.g_szDestination)
            # print("选择的保存路径为：", self.g_szDestination)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = TdWindow()
    myWindow.show()
    sys.exit(app.exec())

