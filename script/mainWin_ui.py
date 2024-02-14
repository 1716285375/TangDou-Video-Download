# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(878, 775)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget\n"
"{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"#frame\n"
"{\n"
"	border-top: 1px solid gray;\n"
"	border-bottom: 1px solid gray;\n"
"}\n"
"/*---------------------------------------------*/\n"
"#label_driver\n"
"{\n"
"	color: rgb(92, 191, 255);\n"
"}\n"
"\n"
"#radioButton_firefox\n"
"{\n"
"	color: #EDCD80;\n"
"}\n"
"#radioButton_google\n"
"{\n"
"	color: #EA9178;\n"
"}\n"
"#radioButton_edge\n"
"{\n"
"	color: #84CFBE;\n"
"}\n"
"/*---------------------------------------------*/\n"
"/*--------------------@\u4f4d\u7f6e\u52a0\u8f7d\u6309\u94ae\uff0c\u6dfb\u52a0\u6309\u94ae@----------------------*/\n"
"#frame_banner\n"
"{\n"
"	background-color: #F8F8F8\n"
"}\n"
"\n"
"#btn_load_driver, #btn_add, #btn_browse\n"
"{\n"
"	color: #fff;\n"
"	background-color: #91a7ff;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"#btn_load_driver:hover, #btn_add:hover, #btn_browse:hover\n"
"{\n"
"	background-color: #6889ff\n"
"}\n"
"\n"
"#btn_load_driver:pressed, #btn_add:pressed, #btn_browse:pressed\n"
"{\n"
"	padding-left: 3px;\n"
""
                        "	padding-top: 3px;\n"
"}\n"
"/*--------------------@\u4f4d\u7f6e\u52a0\u8f7d\u6309\u94ae\uff0c\u6dfb\u52a0\u6309\u94ae@----------------------*/\n"
"/*---------------------------------------------*/\n"
"#btn_cls_list, #btn_cls_table\n"
"{\n"
"	color: #fff;\n"
"	background-color: #f69988;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"#btn_cls_list:hover, #btn_cls_table:hover\n"
"{\n"
"\n"
"	background-color: #d9191d;\n"
"\n"
"}\n"
"\n"
"\n"
"#btn_download\n"
"{\n"
"	color: #fff;\n"
"	background-color: #b388ff;\n"
"	border-radius: 5px;\n"
"}\n"
"#btn_download:hover\n"
"{\n"
"	background-color: #7c4dff;\n"
"}\n"
"\n"
"#btn_cls_list:pressed, #btn_cls_table:pressed, #btn_download:pressed\n"
"{\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"/*---------------------------------------------*/\n"
"/*-------------------@@--------------------*/\n"
"#tableWidget_url\n"
"{\n"
"	color: #546e7a;\n"
"}\n"
"\n"
"#listWidget\n"
"{\n"
"	color: #42BD41;\n"
"}\n"
"\n"
"#textBrowser_output\n"
"{\n"
"	color: #4e342e;\n"
"}\n"
""
                        "/*---------------------@@---------------------*/\n"
"/*---------------------------------------------*/\n"
"#label_download\n"
"{\n"
"	color: #33691e;\n"
"}\n"
"/*---------------------------------------------*/\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_banner = QFrame(self.centralwidget)
        self.frame_banner.setObjectName(u"frame_banner")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_banner.sizePolicy().hasHeightForWidth())
        self.frame_banner.setSizePolicy(sizePolicy)
        self.frame_banner.setFrameShape(QFrame.StyledPanel)
        self.frame_banner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_banner)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_title = QLabel(self.frame_banner)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(30)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)

        self.frame = QFrame(self.frame_banner)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setBold(False)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_driver = QLabel(self.frame)
        self.label_driver.setObjectName(u"label_driver")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_driver.setFont(font2)
        self.label_driver.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.label_driver)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btn_load_driver = QPushButton(self.frame)
        self.btn_load_driver.setObjectName(u"btn_load_driver")
        self.btn_load_driver.setMinimumSize(QSize(70, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_load_driver.setFont(font3)
        self.btn_load_driver.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btn_load_driver)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_firefox = QRadioButton(self.frame)
        self.radioButton_firefox.setObjectName(u"radioButton_firefox")
        font4 = QFont()
        font4.setBold(True)
        self.radioButton_firefox.setFont(font4)
        self.radioButton_firefox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.radioButton_firefox)

        self.radioButton_google = QRadioButton(self.frame)
        self.radioButton_google.setObjectName(u"radioButton_google")
        self.radioButton_google.setFont(font4)
        self.radioButton_google.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.radioButton_google)

        self.radioButton_edge = QRadioButton(self.frame)
        self.radioButton_edge.setObjectName(u"radioButton_edge")
        self.radioButton_edge.setFont(font4)
        self.radioButton_edge.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.radioButton_edge)


        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.label_driver_dir = QLabel(self.frame)
        self.label_driver_dir.setObjectName(u"label_driver_dir")
        self.label_driver_dir.setFont(font1)

        self.gridLayout_5.addWidget(self.label_driver_dir, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_banner)

        self.frame_body = QFrame(self.centralwidget)
        self.frame_body.setObjectName(u"frame_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(8)
        sizePolicy1.setHeightForWidth(self.frame_body.sizePolicy().hasHeightForWidth())
        self.frame_body.setSizePolicy(sizePolicy1)
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_body)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.lineEdit_url = QLineEdit(self.frame_body)
        self.lineEdit_url.setObjectName(u"lineEdit_url")
        self.lineEdit_url.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamilies([u"Consolas"])
        font5.setPointSize(10)
        self.lineEdit_url.setFont(font5)
        self.lineEdit_url.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_url)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_add = QPushButton(self.frame_body)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(50, 20))
        self.btn_add.setFont(font3)
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_add)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.btn_browse = QPushButton(self.frame_body)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(50, 20))
        self.btn_browse.setFont(font3)
        self.btn_browse.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_browse, 0, 0, 1, 1)

        self.label_save_dir = QLabel(self.frame_body)
        self.label_save_dir.setObjectName(u"label_save_dir")
        self.label_save_dir.setFont(font1)

        self.gridLayout.addWidget(self.label_save_dir, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 3)

        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 1)

        self.listWidget = QListWidget(self.frame_body)
        self.listWidget.setObjectName(u"listWidget")
        font6 = QFont()
        font6.setPointSize(10)
        self.listWidget.setFont(font6)

        self.gridLayout_2.addWidget(self.listWidget, 2, 1, 1, 1)

        self.tableWidget_url = QTableWidget(self.frame_body)
        if (self.tableWidget_url.columnCount() < 2):
            self.tableWidget_url.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_url.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_url.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_url.setObjectName(u"tableWidget_url")
        self.tableWidget_url.setFont(font6)
        self.tableWidget_url.setAlternatingRowColors(True)
        self.tableWidget_url.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tableWidget_url, 0, 0, 4, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_all = QCheckBox(self.frame_body)
        self.checkBox_all.setObjectName(u"checkBox_all")
        self.checkBox_all.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.checkBox_all)

        self.btn_cls_table = QPushButton(self.frame_body)
        self.btn_cls_table.setObjectName(u"btn_cls_table")
        self.btn_cls_table.setMinimumSize(QSize(50, 20))
        self.btn_cls_table.setFont(font3)
        self.btn_cls_table.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btn_cls_table)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.btn_download = QPushButton(self.frame_body)
        self.btn_download.setObjectName(u"btn_download")
        self.btn_download.setMinimumSize(QSize(60, 20))
        self.btn_download.setFont(font3)
        self.btn_download.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btn_download)

        self.btn_cls_list = QPushButton(self.frame_body)
        self.btn_cls_list.setObjectName(u"btn_cls_list")
        self.btn_cls_list.setMinimumSize(QSize(50, 20))
        self.btn_cls_list.setFont(font3)
        self.btn_cls_list.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btn_cls_list)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.label_download = QLabel(self.frame_body)
        self.label_download.setObjectName(u"label_download")
        font7 = QFont()
        font7.setFamilies([u"\u5b8b\u4f53"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_download.setFont(font7)
        self.label_download.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_download, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 5)
        self.gridLayout_2.setColumnStretch(1, 4)

        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.widget = QWidget(self.frame_body)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textBrowser_output = QTextBrowser(self.widget)
        self.textBrowser_output.setObjectName(u"textBrowser_output")
        font8 = QFont()
        font8.setPointSize(12)
        self.textBrowser_output.setFont(font8)

        self.gridLayout_3.addWidget(self.textBrowser_output, 0, 0, 3, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 95, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_pro_bar = QLabel(self.widget)
        self.label_pro_bar.setObjectName(u"label_pro_bar")
        font9 = QFont()
        font9.setFamilies([u"Terminal"])
        font9.setPointSize(10)
        font9.setBold(False)
        self.label_pro_bar.setFont(font9)

        self.horizontalLayout_3.addWidget(self.label_pro_bar)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        font10 = QFont()
        font10.setFamilies([u"Consolas"])
        font10.setPointSize(10)
        font10.setBold(False)
        self.progressBar.setFont(font10)
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 94, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 2, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.gridLayout_4.addWidget(self.widget, 2, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_4)


        self.verticalLayout.addWidget(self.frame_body)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u7cd6\u8c46\u89c6\u9891\u4e0b\u8f7d\u5668", None))
        self.label_driver.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6d4f\u89c8\u5668\u9a71\u52a8", None))
        self.btn_load_driver.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u9a71\u52a8", None))
        self.radioButton_firefox.setText(QCoreApplication.translate("MainWindow", u"Firefox", None))
        self.radioButton_google.setText(QCoreApplication.translate("MainWindow", u"Google", None))
        self.radioButton_edge.setText(QCoreApplication.translate("MainWindow", u"Edge", None))
        self.label_driver_dir.setText(QCoreApplication.translate("MainWindow", u"\u9a71\u52a8\u4f4d\u7f6e: ...", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label_save_dir.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4f4d\u7f6e: ...", None))
        ___qtablewidgetitem = self.tableWidget_url.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u9879", None));
        ___qtablewidgetitem1 = self.tableWidget_url.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None));
        self.checkBox_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
        self.btn_cls_table.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4e0b\u8f7d", None))
        self.btn_cls_list.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label_download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5217\u8868", None))
        self.textBrowser_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_pro_bar.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u8fdb\u5ea6", None))
    # retranslateUi

