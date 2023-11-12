import requests
import os

if __name__ == "__main__":
    file = open("./main.exe", 'wb')
    file.write(requests.get("https://github.cooluc.com/https://github.com/Jaffrez/seewo_tools/releases/download/master/seewo_tools_setup.exe").content)
    file.close()
    os.execl("./main.exe", "main.exe","")