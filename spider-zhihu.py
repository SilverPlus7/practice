__author__ = 'hzwer'
# -*- coding: utf-8 -*-

import re
import gzip
import requests
import http.cookiejar
import urllib.request
import urllib.parse

def ungzip(data):
    try:
        print ('解压gzip\n')
        data = gzip.decompress(data)
        print ('OK\n')
    except:
        print ('无需解压')
    return data

head = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
    'Connection': 'keep-alive',
    'Host': 'www.zhihu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def getxsrf(data):
    str = re.compile('name=\"_xsrf\" value=\"(.*)\"')
    res = str.findall(data)[0]
    return res

class Spider:

    def __init__(self):
        self.url = 'http://www.zhihu.com/login/email'
        cookie = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        # create cookie

        response = self.opener.open(self.url)
        content = response.read().decode('UTF-8')
        _xsrf = getxsrf(content)
        # get _xsrf

        email = input('your email ')
        password = input('your password ')
        self.post = {
            '_xsrf': _xsrf,
            'password': password,
            'remember_me': 'true',
            'email': email
        }

    def login(self):
        header = []
        for key,value in head.items():
            header.append((key,value))
        self.opener.addheaders = header
        post = urllib.parse.urlencode(self.post).encode()
        response = self.opener.open(self.url, post)
        data = response.read()
        data = ungzip(data)
        print (data.decode())

spider=Spider()
spider.login()
