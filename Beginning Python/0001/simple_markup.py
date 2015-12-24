#简单的标记程序
import re
import sys
from util import *

print ('<html><head><title>hzwer</title></head><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub('\*(.+?)\*','<em>\l</em>',block)
    if title:
        print ('<h1>')
        print (block)
        print ('</h1>')
        title = False
    else:
        print ('<p>')
        print (block)
        print ('</p>')

print ('</body></html>')
