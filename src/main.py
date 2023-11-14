from mainWindow import MainWindow
from PySide6 import QtGui,QtWidgets,QtCore
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())