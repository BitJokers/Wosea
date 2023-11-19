'''
Author: Jaffrez Jaffrez@outlook.com
Date: 2023-11-16 22:30:37
LastEditors: Jaffrez Jaffrez@outlook.com
LastEditTime: 2023-11-19 15:22:49
FilePath: /Wosea/src/update.py
Description: 更新模块
Copyright (c) 2023 by Jaffrez, All Rights Reserved.
'''

import wget
import os

if __name__:
    url = "https://github.cooluc.com/https://github.com/Jaffrez/\
        seewo_tools/releases/download/master/main.exe"

    wget.download(url, '.\\main.exe')
    os.execl("./main.exe", "main.exe", "")
