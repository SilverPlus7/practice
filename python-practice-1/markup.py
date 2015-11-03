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
