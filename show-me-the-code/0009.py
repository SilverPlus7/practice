# coding: utf-8
# 第 0009 题：一个HTML文件，找出里面的链接。
# 使用正则表达式

import re
from urllib.request import *

keywords = ['css', 'java', '#', '%', '@', 'jpg', 'png', 'gif', 'ico']
def check(link):
    for word in keywords:
        if word in link:
            return False
    return True

url = 'http://hzwer.com'
target = 'http://hzwer.com/'

request = Request(target)
respond = urlopen(request)
content = respond.read().decode("UTF-8")

pattern = re.compile('href="(.*?)"',re.S)
res = re.findall(pattern, content)

for link in res:
    if link[0] == '/':
        link = url + link
    if check(link):
        print(link)
