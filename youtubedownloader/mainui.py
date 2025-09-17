# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(492, 302)
        MainWindow.setMinimumSize(QSize(492, 302))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 471, 232))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.down_fd = QToolButton(self.verticalLayoutWidget)
        self.down_fd.setObjectName(u"down_fd")

        self.gridLayout.addWidget(self.down_fd, 2, 2, 1, 1)

        self.down = QLineEdit(self.verticalLayoutWidget)
        self.down.setObjectName(u"down")

        self.gridLayout.addWidget(self.down, 2, 1, 1, 1)

        self.label_url = QLabel(self.verticalLayoutWidget)
        self.label_url.setObjectName(u"label_url")

        self.gridLayout.addWidget(self.label_url, 0, 0, 1, 1)

        self.labe_down = QLabel(self.verticalLayoutWidget)
        self.labe_down.setObjectName(u"labe_down")

        self.gridLayout.addWidget(self.labe_down, 2, 0, 1, 1)

        self.url = QLineEdit(self.verticalLayoutWidget)
        self.url.setObjectName(u"url")

        self.gridLayout.addWidget(self.url, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.download = QPushButton(self.verticalLayoutWidget)
        self.download.setObjectName(u"download")

        self.verticalLayout.addWidget(self.download)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 492, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.down_fd.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_url.setText(QCoreApplication.translate("MainWindow", u"Video URL", None))
        self.labe_down.setText(QCoreApplication.translate("MainWindow", u"Download location", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"Download!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"A very basic YT-DLP frontend", None))
    # retranslateUi

