#!/usr/bin/env python
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QSortFilterProxyModel
from ui.mainwindow import Ui_MainWindow
from models.packagetable import InstallTable, UpdateTable
from pacman_wrapper import fetch_all_packages, fetch_updates

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Pacman-Front")

        #------------#
        # Update tab #
        #------------#

        # Initializing the update table model with updateable packages on the system
        updateListModel = UpdateTable(fetch_updates())

        # Pressing the update button passes the model containing the updateable packages to the table view
        self.updatefetch.clicked.connect(lambda: self.packagelist.setModel(updateListModel))

        #-------------#
        # Install tab #
        #-------------#

        # Initializing the install table model with every package available in the repos
        installListModel = InstallTable(fetch_all_packages())

        # Proxy model necessary for the search functionality to work
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(installListModel)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setFilterKeyColumn(0)  

        # Passing the proxy model to the table view
        self.pkglist.setModel(self.proxy_model)

        # Pressing the search button filters the proxy model with the current string in the search bar
        self.searchbutton.clicked.connect(lambda text: self.proxy_model.setFilterFixedString(self.searchbar.text()))


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()