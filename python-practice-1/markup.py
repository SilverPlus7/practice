import re
import sys
from util import *
from handlers import *

class Parser:
    # 语法分析器，读取文本，应用规则并且控制处理程序
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
        
    def add_rule(self, rule):
        self.rules.append(rule)

    def add_filter(self, pattern, name):
    # self.add_filter('(\*(.+?)\*','emphasis')
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
        for rule in self.rules:
            if rule.action(block, self.handler):
                break
        self.handler.end('document')

class basic_text_parser(Parser):
    Parser.__init__(self, handler)
    def __init__(self, handler):
        self.add_rule(list_rule())
        self.add_rule(listitem_rule())
        self.add_rule(title_rule())
        self.add_rule(heading_rule())
        self.add_rule(paragraph_rule())
        
        self.add_filter('(\*(.+?)\*','emphasis')
        self.add_filter('(http://[\.a-zA-Z/]+)', 'url')
        self.add_filter('([\.a-zA-Z/]+@[\.a-zA-Z/]+[a-z]+)','mail')
        
handler = HTML_renderer()
parser = basic_text_parser(handler)

parser.parse(sys.stdin)
