import time
from datetime import datetime

hosts_temp = "hostsTest"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirectIP = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]


def WebsiteBlocker():
    while True:
        if isCheckTime():
            print("Working hours...")
            with open(hosts_path, "r+") as file:
                content = file.read()
                if not isWebsitesInContent(content, website_list):
                    WriteURLToFile(website_list, file)
        else:
            print("Fun hours...")
            with open(hosts_path, "r+") as file:
                content = file.read()
                if isWebsitesInContent(content, website_list):
                    ReturnFileToNormal(website_list, file)
        time.sleep(10)


def ReturnFileToNormal(_website_list, _file):
    _file.seek(0)
    _content = _file.readlines()
    _file.seek(0)
    for line in _content:
        if not any(website in line for website in _website_list):
            _file.write(line)
    _file.truncate()


def WriteURLToFile(_website_list, _file):
    for website in _website_list:
        _file.write("\n" + redirectIP + " " + website)


def isCheckTime():
    if 22 > datetime.now().hour > 10:
        return True
    else:
        return False


def isWebsitesInContent(_content, _website_list):
    for website in _website_list:
        return website in _content


if __name__ == '__main__':
    WebsiteBlocker()
