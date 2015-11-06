import re
import sys
from util import *
from rules import *
from handlers import *

class Parser:
    # 语法分析器，读取文本，应用规则并且控制处理程序
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.Filters = []
        
    def add_rule(self, rule):
        self.rules.append(rule)

    def add_Filter(self, pattern, name):
    # self.add_Filter('(\*(.+?)\*','emphasis')
        def Filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.Filters.append(Filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for Filter in self.Filters:
                block = Filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    if rule.action(block, self.handler):
                        break
        self.handler.end('document')

class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.add_rule(ListRule())
        self.add_rule(ListItemRule())
        self.add_rule(TitleRule())
        self.add_rule(HeadingRule())
        self.add_rule(ParagraphRule())
        
        self.add_Filter('\*(.+?)\*','emphasis')
        self.add_Filter('(http://[\.a-zA-Z/]+)', 'url')
        self.add_Filter('([\.a-zA-Z/]+@[\.a-zA-Z/]+[a-z]+)', 'mail')
        
handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
