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
        self.centralwidget.setMinimumSize(QSize(800, 500))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.updateview = QTableView(self.centralwidget)
        self.updateview.setObjectName(u"updateview")

        self.verticalLayout.addWidget(self.updateview)

        self.fetchupdate = QPushButton(self.centralwidget)
        self.fetchupdate.setObjectName(u"fetchupdate")

        self.verticalLayout.addWidget(self.fetchupdate)

        self.updatebutton = QPushButton(self.centralwidget)
        self.updatebutton.setObjectName(u"updatebutton")

        self.verticalLayout.addWidget(self.updatebutton)

        self.pacmanoutput = QPlainTextEdit(self.centralwidget)
        self.pacmanoutput.setObjectName(u"pacmanoutput")
        self.pacmanoutput.setReadOnly(True)

        self.verticalLayout.addWidget(self.pacmanoutput)


        self.verticalLayout_2.addLayout(self.verticalLayout)

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

