"""
简单介绍一下我的思路，其实大家用的应该都是同样的思路。
首先是获取视频的链接，这里直接随便复制一个即可，然后右键获得网页源代码，查找window.__playinfo这个js文件，之后里面就有这个视频的详细信息了。
所以我们首先是通过requests获取网页源代码，然后请求对应的视频链接，这里其实他的json文件中有audio和video两个对应的内容，分别是音频和视频。
我们直接请求下面的第一个数组的数据即可，也就是第一个的baseUrl，然后对该链接进行请求即可。
但是实际上如果只是这么请求的话，是获取不到数据的，这是因为B站使用了防盗链，如果你不是从bilibili进行访问的话，他会对你进行拦截，所以我们要在headers
中添加防盗链，然后进行请求即可，之后将文件写入本地再通过ffmpeg来进行合成，当然用别的也可以，什么pr剪影啥的，都可以，直接将素材导入然后合并就行了，
但是实际上确实没有ffmpeg方便。如果要使用ffmpeg的话，记得将他写入环境变量里。
"""

"""
这里再强推一下jupyter notebook，真的是太舒服了，特别是用selenium，我觉得是真的太舒服了。
"""
import requests
import re
import json
import subprocess

# 这里其实可以考虑用一下随机ua，不过我只是做一个测试而已，所以只是随便复制了一下。
header = {
    "referer": "https://www.bilibili.com/",  # 防盗链
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
}

url = "https://www.bilibili.com/video/BV1UQ4y1k7dG"  # 假如不健身违法
res = requests.get(url, headers=header)
result = re.findall("window.__playinfo__=(.*?)</script>", res.text)  # 通过正则查找对应数据
json_data = json.loads(result[0])  # 将数据转化成json模式
video_url = json_data['data']['dash']['video'][0]['baseUrl']  # 获取视频的链接
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']  # 获取音频的链接
title = re.findall('<h1 title="(.*?)" class="video-title">', res.text)[0]  # 获取视频标题
video_content = requests.get(video_url, headers=header).content  # 获取二进制数据 好写入本地
audio_content = requests.get(audio_url, headers=header).content  # 图片音频视频之类的是获取二进制数据来写入的

title = re.findall('【(.*?)】', title)  # 写入本地 将标题进行提取  什么去掉括号之类的，不过我这里其实只写了匹配我这个视频的，具体的请自己思考
title = title[0].replace(' ', '')
with open(title+'.mp3', 'wb') as file:  # 写入数据
    file.write(audio_content)
with open(title+'.mp4', 'wb') as file:
    file.write(video_content)
print("视频开始合并")
COMMAND = f'ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental {title}total.mp4'
subprocess.Popen(COMMAND, shell=True)  # 这里用的是Popen，就是说它运行在后台，多线程。也可以用下面的run，就是单线程
# subprocess.run(COMMAND)
print('视频合并结束')
