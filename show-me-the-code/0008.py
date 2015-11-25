# coding: utf-8
# 第 0008 题：一个HTML文件，找出里面的正文。
# 使用Python-goose项目
# python版本:2.6

from goose import Goose
from goose.text import StopWordsChinese

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 设置系统默认编码

url = raw_input('url: ')
print url

g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url = url)
print article.cleaned_text.decode("utf-8")

