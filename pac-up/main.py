from PySide6 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from models.update_list_model import UpdateTableModel
from helpers.pacman import fetch_updates, update

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Hook up model for the update table view
        def fill_update_table():
            self.updateview.model = UpdateTableModel(fetch_updates())
            self.updateview.setModel(self.updateview.model)

        # Refresh model data with output of pacman -Qu, blank out previous pacman output
        self.fetchupdate.clicked.connect(fill_update_table)
        self.fetchupdate.clicked.connect(lambda: self.pacmanoutput.setPlainText(""))

        # Update the packages listed in the update table view
        self.updatebutton.clicked.connect(lambda: self.pacmanoutput.setPlainText(update(self.updateview.model.get_packagenames())))

        # Grey out update button if there are no packages to update
        def are_there_updates():
            if not self.updateview.model.get_packagenames():
                self.updatebutton.setText("Up to date")
                self.updatebutton.setEnabled(False)
            else:
                self.updatebutton.setText("Update")
                self.updatebutton.setEnabled(True)

        # Execute the previous function whenever the update view is refreshed
        self.fetchupdate.clicked.connect(are_there_updates)

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
