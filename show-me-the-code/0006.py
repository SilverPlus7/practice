# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# 输出当前目录下每篇文章的关键词

import sys, os

def run(file):
    f = open('./' + file, 'r')
    stop_word = ['the', 'and',  'has', 'that', 'are', 'with', 'what', 'not', 'can', 'but' ,'you', 'they', 'she', 'also', 'one', 'much', 'more', 'very', 'from']
    words = []
    dict = {}

    for line in f:
        line = ' '.join(line.split('.'))
        line = ' '.join(line.split(','))
        line = ' '.join(line.split('?'))
        line = ' '.join(line.split('-'))
        line = ' '.join(line.split('!'))
        line = ' '.join(line.split('\''))
        words += line.strip().split(' ')

    f.close()
    
    for word in words:
        word = word.lower()
        if(word not in dict):
            dict[word] = 1
        else:
            dict[word] = dict[word] + 1

    ans = ''
    dict[ans] = 0
    for key, value in dict.items():
        if(key not in stop_word and len(key) > 2 and value > dict[ans]):
            ans = key
    return ans 

for file in os.listdir(os.getcwd()):
    if os.path.splitext(file)[1] == '.txt':
        print('《{} 》的关键词是{}'.format(file[0], run(file)))
