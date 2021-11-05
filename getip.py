import requests
from lxml import etree
from time import sleep
from fake_useragent import UserAgent

ua = UserAgent()
ua = ua.chrome
# url = 'https://www.bilibili.com/'
# headers = {
#     'User-agent': ua,
#     "referer": "https://www.bilibili.com/"
# }
# with open('ip.txt','r') as file:
#     ip = file.readlines()
# dl = []
# for i in ip:
#     i = str(i.strip())
#     proxies = {
#         'http': "http://"+i,
#         'https': "http://" + i
#     }
#     try:
#         get = requests.get(url, headers=headers, proxies=proxies, timeout=1)
#         if get.status_code == 200:
#             print(1)
#             dl.append(i)
#             with open('ipsuccess.txt', 'a') as file:
#                 file.write(i)
#                 file.write('\n')
#     except:
#         print(i+"失败")
# print(dl)

# def
url = "http://icanhazip.com/"
headers = {
    "User-agent": ua,
}
proxies = {
"http":"http://113.204.239.91:8081",
"https":"http://113.204.239.91:8081"
}
get = requests.get(url, headers=headers, proxies=proxies, timeout=2)

print(get.text)