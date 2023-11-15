
from PySide6 import QtGui,QtWidgets,QtCore
import sys

import PySide6.QtCore
import PySide6.QtWidgets
from mainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon("./icon.png"))
    window.show()

    sys.exit(app.exec())