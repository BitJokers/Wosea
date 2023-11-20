'''
Author: Jaffrez Jaffrez@outlook.com
Date: 2023-11-16 23:04:27
LastEditors: Jaffrez Jaffrez@outlook.com
LastEditTime: 2023-11-19 15:24:24
FilePath: /Wosea/src/closeEasiNote.py
Description: 关闭希沃白板
Copyright (c) 2023 by Jaffrez, All Rights Reserved.
'''
import os


def closeEasiNote():
    # FIXME： 修复当希沃没有开启时没有提示
    # 这个实在不好修,先不修了.
    os.system("taskkill -F /im EasiNote.exe")
