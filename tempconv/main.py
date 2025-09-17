from PySide6 import QtWidgets
import sys
from tempui import Ui_MainWindow
from converter import convert

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("TempConv")


        self.c_box.textEdited.connect(
            lambda text: self.f_box.setText(convert(self.c_box))
        )

        self.f_box.textEdited.connect(
            lambda text: self.c_box.setText(convert(self.f_box))
        )

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()