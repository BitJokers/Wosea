import os

def closeEasiNote():
    # FIXME： 修复当希沃没有开启时没有提示
    os.system("taskkill -F /im EasiNote.exe")