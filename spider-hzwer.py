# 统计博客hzwer.com上的代码行数

__author__ = 'hzwer'
# -*- coding: utf-8 -*-  

import re
from urllib.request import *

home = 'http://hzwer.com/'
tot = 0
page = 0

for i in range(1, 8000):
    try:
        url = home + str(i) + '.html'
        request = Request(url)
        response = urlopen(request)
        content = response.read().decode("UTF-8").replace("\r\n", "\n")
    except:
        pass
    else:
        pattern = re.compile('-webkit-tab-size:4; tab-size:4; font-size: 15px !important; line-height: 16px !important;">\n(.*?)</textarea>', re.S)
        code = re.findall(pattern, content)
        if(code):
            length = 0
            for j in code:
                length = length + len(j.splitlines())
            tot += length
            print('url: {} {}行代码，合计{}行代码'.format(url, length, tot))
            page = page + 1

print('共{}个页面，{}行代码'.format(page, tot))
