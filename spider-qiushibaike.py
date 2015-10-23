__author__ = 'hzwer'
# -*- coding: utf-8 -*-  

import urllib.request
import re

class spider:
    def __init__(self):
        self.page = 1
        #记录访问的页码
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        #伪装浏览器君
        self.headers = { 'User-Agent' : self.user_agent }
        self.stories = []
        #存储段子

    def get_stories(self):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(self.page)
            request = urllib.request.Request(url,headers = self.headers)
            #构建request
            self.page += 1
            #翻页
            response = urllib.request.urlopen(request)
            content = response.read().decode("UTF-8").replace("<br/>","\n")
            #编码转化，转换换行符
            pattern = re.compile('jpg" />\n(.*?)\n</a>.*?"content">\n\n(.*?)\n<!--(.*?)"number">(.*?)</i> 好笑',re.S)
            self.stories = re.findall(pattern,content)
            #正则表达式匹配
            
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print (u"获取失败，错误原因",e.reason) 
                #错误信息
                return None

    def start(self):
        print (u"正在读取糗事百科\n")
        while True:
            self.get_stories()
            #获取一页段子
            for story in self.stories:
                #遍历段子
                if not re.search('img',story[2]):
                #去除带图段子
                    Input = input("回车查看新段子,Q 键退出程序")
                    #用户键入
                    if Input == 'Q' or Input == 'q':
                        print("下次再见")
                        return
                    print (u"第%d页 作者:%s 赞数%s\n%s\n" %(self.page-1,story[0],story[3],story[1]))
            print("翻个页 TwT\n")
spider = spider()
spider.start()        
