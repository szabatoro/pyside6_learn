from posix import open
from PySide6 import QtWidgets
from mainui import Ui_MainWindow
import sys
from downloader import download

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Youtube Downloader")

        self.down_fd.clicked.connect(self.open_folder_dialog)

        self.download.clicked.connect(
            lambda : download(self.url.text(), self.down.text(), self.progress_hook)
        )

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d['downloaded_bytes']
            percent = int(downloaded / total * 100)
            self.progressBar.setValue(percent)

    def open_folder_dialog(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder", "")
        if folder:
            self.down.setText(folder)



window = MainWindow()
window.show()
app.exec()
