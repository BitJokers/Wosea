import os


def closeEasiNote():
    # FIXME： 修复当希沃没有开启时没有提示
    # 这个实在不好修,先不修了.
    os.system("taskkill -F /im EasiNote.exe")
