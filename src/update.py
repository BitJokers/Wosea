import wget
import os

if __name__:
    url = "https://github.cooluc.com/https://github.com/Jaffrez/\
        seewo_tools/releases/download/master/main.exe"

    wget.download(url, '.\\main.exe')
    os.execl("./main.exe", "main.exe", "")
