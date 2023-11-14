import requests
import os
from PySide6 import QtWidgets

if __name__:
    req = requests.get("https://github.cooluc.com/https://github.com/Jaffrez/seewo_tools/releases/download/master/main.exe")
    if not req.status_code == 200:
        QtWidgets.QMessageBox(None,"更新失败", "更新失败")
        os.execl("./main.exe", "main.exe","")
    file = open("./main.exe", 'wb')
    file.write()
    file.close()
    os.execl("./main.exe", "main.exe","")