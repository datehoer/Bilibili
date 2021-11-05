import requests,json
from fake_useragent import UserAgent

ua = UserAgent()
ua = ua.chrome

headers = {
    "User-agent": ua,
    "referer":"https://www.bilibili.com"
}
# proxies = {
#     "http":"http://14.163.157.247:9999",
# "https":"http://14.163.157.247:9999"
# }
import re
url = 'https://www.bilibili.com/video/BV1Wf4y157tj?p=1'
# bv = requests.get(url, headers=headers, proxies=proxies,timeout=1)
bv = requests.get(url, headers=headers, timeout=1)
pattern =re.compile(r'/video/(.*)\?p')
bv = pattern.findall(bv.url)

print(bv)

avapi = "http://api.bilibili.com/x/web-interface/archive/stat?bvid="

# av = requests.get(avapi+bv[0],headers=headers, proxies=proxies)
av = requests.get(avapi+bv[0],headers=headers, timeout=1)
av = json.loads(av.text)['data']['aid']

cvapi = "https://api.bilibili.com/x/web-interface/view?aid="

# cv = requests.get(cvapi+str(av),headers=headers, proxies=proxies)
cv = requests.get(cvapi+str(av),headers=headers, timeout=1)
cv = json.loads(cv.text)

cv = cv['data']['pages'][0]['cid']

downloadurl = "https://api.bilibili.com/x/player/playurl?avid="

# url = requests.get(downloadurl+str(av)+"&cid="+str(cv)+"&qn=112", headers=headers, proxies=proxies)
url = requests.get(downloadurl+str(av)+"&cid="+str(cv)+"&qn=112",timeout=1, headers=headers)
url = json.loads(url.text)
url = url['data']['durl'][0]['url']

# download = requests.get(url, headers=headers, proxies=proxies)
download = requests.get(url, headers=headers)
with open("shipin.mp4",'wb') as file:
    file.write(download.content)
