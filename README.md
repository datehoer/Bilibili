Python Bilibili mp4

>　首先感谢一下b站，给我这样的野生程序员一条学习的道路。
其次感谢Python，给我一条吃饭的道路。
最后感谢各种大牛，给我提供了许许多多的便捷库。

需要用到的环境有：

1. Python 3.8
2. ffmpeg

需要运用到的Python库有：
1. requests
2. re
3. json
4. subprocess

简单说明一下，首先Python版本应该都行吧，Python3的即可，当然Python2的话也可能行，推荐使用Python3。

然后ffmpeg是一个合成音频视频的一个小工具，用起来其实比较的舒服。
download:https://www.ffmpeg.org/

最后简单介绍一下这些库的作用吧：
1. requests---请求库，获取数据
2. re---正则表达式，获取对应的数据
3. json---json库，将对应的字符串转化成json数据
4. subprocess---多线程，执行cmd指令合成视频