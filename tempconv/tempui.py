# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(259, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 241, 271))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.f_box = QLineEdit(self.gridLayoutWidget)
        self.f_box.setObjectName(u"f_box")

        self.gridLayout.addWidget(self.f_box, 0, 0, 1, 1)

        self.c_box = QLineEdit(self.gridLayoutWidget)
        self.c_box.setObjectName(u"c_box")

        self.gridLayout.addWidget(self.c_box, 1, 0, 1, 1)

        self.f_label = QLabel(self.gridLayoutWidget)
        self.f_label.setObjectName(u"f_label")

        self.gridLayout.addWidget(self.f_label, 0, 1, 1, 1)

        self.c_label = QLabel(self.gridLayoutWidget)
        self.c_label.setObjectName(u"c_label")

        self.gridLayout.addWidget(self.c_label, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.f_label.setText(QCoreApplication.translate("MainWindow", u"Fahrenheit", None))
        self.c_label.setText(QCoreApplication.translate("MainWindow", u"Celsius", None))
    # retranslateUi

