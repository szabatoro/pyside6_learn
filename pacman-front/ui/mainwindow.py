# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 781, 521))
        self.updater = QWidget()
        self.updater.setObjectName(u"updater")
        self.verticalLayoutWidget = QWidget(self.updater)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 761, 471))
        self.upd_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.upd_layout.setObjectName(u"upd_layout")
        self.upd_layout.setContentsMargins(0, 0, 0, 0)
        self.packagelist = QTableView(self.verticalLayoutWidget)
        self.packagelist.setObjectName(u"packagelist")

        self.upd_layout.addWidget(self.packagelist)

        self.updatefetch = QPushButton(self.verticalLayoutWidget)
        self.updatefetch.setObjectName(u"updatefetch")

        self.upd_layout.addWidget(self.updatefetch)

        self.update = QPushButton(self.verticalLayoutWidget)
        self.update.setObjectName(u"update")

        self.upd_layout.addWidget(self.update)

        self.tabWidget.addTab(self.updater, "")
        self.installer = QWidget()
        self.installer.setObjectName(u"installer")
        self.verticalLayoutWidget_2 = QWidget(self.installer)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 10, 761, 471))
        self.inst_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.inst_layout.setObjectName(u"inst_layout")
        self.inst_layout.setContentsMargins(0, 0, 0, 0)
        self.pkglist = QTableView(self.verticalLayoutWidget_2)
        self.pkglist.setObjectName(u"pkglist")

        self.inst_layout.addWidget(self.pkglist)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchbar = QLineEdit(self.verticalLayoutWidget_2)
        self.searchbar.setObjectName(u"searchbar")

        self.horizontalLayout_2.addWidget(self.searchbar)

        self.searchbutton = QPushButton(self.verticalLayoutWidget_2)
        self.searchbutton.setObjectName(u"searchbutton")

        self.horizontalLayout_2.addWidget(self.searchbutton)


        self.inst_layout.addLayout(self.horizontalLayout_2)

        self.install = QPushButton(self.verticalLayoutWidget_2)
        self.install.setObjectName(u"install")

        self.inst_layout.addWidget(self.install)

        self.tabWidget.addTab(self.installer, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.updatefetch.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.updater), QCoreApplication.translate("MainWindow", u"Updater", None))
        self.searchbar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for the package you want to install", None))
        self.searchbutton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.install.setText(QCoreApplication.translate("MainWindow", u"Install selected packages", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.installer), QCoreApplication.translate("MainWindow", u"Installer", None))
    # retranslateUi

