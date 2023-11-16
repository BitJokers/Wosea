
from PySide6 import QtGui,QtWidgets,QtCore
import sys
import PySide6.QtCore
import PySide6.QtWidgets
from mainWindow import Ui_MainWindow
import numGen
import closeEasiNote

class aboutWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel("本软件由Jaffrez&Bloid-Cook制作", self, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.closeButton = QtWidgets.QPushButton("关闭",self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.closeButton)

        self.closeButton.clicked.connect(self.close)
    def close(self):
        self.destroy()

def showAbout():
    root = aboutWindow()
    root.show()
class MainWindow(QtWidgets.QMainWindow):
    def exit(self):
        self.destroy()
        sys.exit()
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.genNumButton.clicked.connect(numGen.start)
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.closeSeewoNoteButton.clicked.connect(closeEasiNote.closeEasiNote)
        # FIXME： 修复关于页面无法打开
        self.ui.aboutButton.clicked.connect(showAbout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon("./icon.png"))
    window.show()

    sys.exit(app.exec())