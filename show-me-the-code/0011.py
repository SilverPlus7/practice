# coding: utf-8
# 敏感词文本文件 filtered_words.txt，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
import sys

words = []
def check():
    while True:
        try:
            word = str(raw_input())
        except:
            break
        if word in words:
            return False
    return True

file = open('./filtered_words.txt', 'r')
for word in file:
    words.append(word.strip())
file.close()

if check():
    print('Freedom')
else:
    print('Human Rights')
