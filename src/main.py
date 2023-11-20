'''
Author: Jaffrez Jaffrez@outlook.com
Date: 2023-11-14 12:38:41
LastEditors: Jaffrez Jaffrez@outlook.com
LastEditTime: 2023-11-19 15:23:52
FilePath: /Wosea/src/main.py
Description:
Copyright (c) 2023 by Jaffrez, All Rights Reserved.
'''
from PySide6 import QtGui, QtWidgets
import sys
from mainWindow import Ui_MainWindow
import numGen
import closeEasiNote


# 关于窗口
class aboutDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("关于")

        self.buttonbox = QtWidgets\
            .QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonbox.accepted.connect(self.accept)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(QtWidgets.QLabel("本软件由Jaffrez & Bloid-Cook 开发"))
        self.layout.addWidget(self.buttonbox)
        self.setLayout(self.layout)


# 显示about页面
def showAbout():
    dialog = aboutDialog()
    dialog.exec()


# 这是主窗口
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
        self.ui.closeSeewoNoteButton.clicked.\
            connect(closeEasiNote.closeEasiNote)
        self.ui.aboutButton.clicked.connect(showAbout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon("./icon.png"))
    window.show()

    sys.exit(app.exec())
