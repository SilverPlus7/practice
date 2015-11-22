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
