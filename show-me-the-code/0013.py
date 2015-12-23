# coding: utf-8
# 用 Python 写一个爬百度贴吧帖子图片的程序
# 使用正则表达式
# 图片保存在当前目录的新建文件夹tieba_img内

import re
import os
import requests
   
img = []
path = './tieba_img/'
os.system('rm -r tieba_img')
os.system('mkdir tieba_img')

def get_img(content):
    pattern = re.compile('src="http://imgsrc.baidu.com/(.*?)" ', re.S)
    img.extend(re.findall(pattern, content))

    count = 0
    for imgurl in img:
        imgurl = 'http://imgsrc.baidu.com/' + imgurl
        r = requests.get(imgurl)
        if r.url != 'http://hiphotos.baidu.com/error.html':
            count += 1
            f = open(path + str(count) + '.jpg', 'wb')
            f.write(r.content)
            f.close()
            print('正在下载第' + str(count) + '张图片')

url = input('url ')
r = requests.get(url)

get_img(r.text)
os.system('open ' + path)
