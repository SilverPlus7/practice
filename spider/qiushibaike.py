__author__ = 'hzwer'
# -*- coding: utf-8 -*-  

import re
from urllib.request import *

class Spider:
    def __init__(self):
        self.page = 1
        # 记录访问的页码
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        # 伪装浏览器君
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        # 存储段子

    def get_stories(self):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(self.page)
            request = Request(url, headers = self.headers)
            # 构建request
            self.page += 1
            # 翻页
            response = urlopen(request)
            content = response.read().decode("UTF-8").replace("<br/>", "\n")
            pattern = re.compile('alt="(.*?)".*?"content">\n(.*?)<!--(.*?)"number">(.*?)</i> 好笑', re.S)
            # 作者， 可能存在的图片信息， 内容， 赞数
            self.stories = re.findall(pattern, content)
            # 正则表达式匹配
            
        except URLError as e:
            if hasattr(e, "reason"):
                print ("获取失败，错误原因", e.reason) 
                # 错误信息
                return None
    def start(self):
        print ("{:^70}".format('正在读取糗事百科'))
        while True:
            self.get_stories()
            # 获取一页段子
            for story in self.stories:
                # 遍历段子
                if not re.search('img', story[2]):
                # 去除带图段子
                    Input = input("{:^70}".format('回车查看新段子, Q 键退出程序\n'))
                    # 用户键入
                    if Input is 'Q' or Input is 'q':
                        print ("{:^70}".format('再见'))
                        return
                    print ('{:^70}'.format('第{}页 作者:{} 赞数{}').format(self.page-1, story[0], story[3]))
                    print ('{}\n'.format(story[1]))
            print ("{:^70}".format('翻个页 TwT'))
spider = Spider()
spider.start()
