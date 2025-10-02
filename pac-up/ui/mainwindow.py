# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 781, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.updateview = QTableView(self.verticalLayoutWidget)
        self.updateview.setObjectName(u"updateview")

        self.verticalLayout.addWidget(self.updateview)

        self.fetchupdate = QPushButton(self.verticalLayoutWidget)
        self.fetchupdate.setObjectName(u"fetchupdate")

        self.verticalLayout.addWidget(self.fetchupdate)

        self.updatebutton = QPushButton(self.verticalLayoutWidget)
        self.updatebutton.setObjectName(u"updatebutton")

        self.verticalLayout.addWidget(self.updatebutton)

        self.pacmanoutput = QPlainTextEdit(self.verticalLayoutWidget)
        self.pacmanoutput.setObjectName(u"pacmanoutput")
        self.pacmanoutput.setReadOnly(True)

        self.verticalLayout.addWidget(self.pacmanoutput)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pac-Up", None))
        self.fetchupdate.setText(QCoreApplication.translate("MainWindow", u"Fetch updates", None))
        self.updatebutton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pacmanoutput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pacman update output will be printed here...", None))
    # retranslateUi

