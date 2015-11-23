# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
# 统计标准输入文本的单词出现次数

import sys

words = []
dict = {}

for line in sys.stdin:

    line = ' '.join(line.split('.'))
    line = ' '.join(line.split(','))
    line = ' '.join(line.split('?'))
    line = ' '.join(line.split('-'))
    line = ' '.join(line.split('!'))
    line = ' '.join(line.split('\''))

    words += line.strip().split(' ')

for word in words:
    word = word.lower()
    if(word not in dict):
        dict[word] = 1
    else:
        dict[word] = dict[word] + 1

for key, value in dict.items():
    if(key):
        print('{} {}'.format(key, value))
