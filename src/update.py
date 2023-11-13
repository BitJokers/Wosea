import requests
import os
from PySide6 import QtCore, QtWidgets,QtGui

if __name__ == "__main__":
    try:
        req = requests.get("https://github.cooluc.com/https://github.com/Jaffrez\
                            /seewo_tools/releases/download/master/main.exe")
        # 检验状态码
        if not req.status_code == 200:
            raise TimeoutError
    except:
        QtWidgets.QMessageBox(None,"更新失败", "更新失败")
        os.execl("./main.exe", "main.exe","") # 覆盖原进程
    file = open("./main.exe", 'wb')
    file.write()
    file.close()
    os.execl("./main.exe", "main.exe","")