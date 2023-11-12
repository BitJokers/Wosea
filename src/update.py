import requests
import os
from PySide6 import QtCore, QtWidgets,QtGui

if __name__ == "__main__":
    req = requests.get("https://github.cooluc.com/https://github.com/Jaffrez\
                            /seewo_tools/releases/download/master/seewo_tools_setup.exe")
    if not req.status_code == 200:
        QtWidgets.QMessageBox(None,"更新失败", "更新失败")
        os.execl("./main.exe", "main.exe","")
    file = open("./main.exe", 'wb')
    file.write()
    file.close()
    os.execl("./main.exe", "main.exe","")