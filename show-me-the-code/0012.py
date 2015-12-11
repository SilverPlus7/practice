# coding: utf-8
# 敏感词文本文件 filtered_words.txt，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」
import sys

words = []
def filter():
    while True:
        try:
            word = str(raw_input())
        except:
            break
        for filetered_word in words:
            word = word.replace(filetered_word, '**')
        print(word)

file = open('./filtered_words.txt', 'r')
for word in file:
    words.append(word.strip())
file.close()

filter()
