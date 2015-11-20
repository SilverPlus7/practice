# 第 0001 题：作为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 方法: id(1-1000, 转16进制) + 'L' + 随机字符串
#（虽然觉得很不靠谱）

import random, string

def get_code(key): # id转code
    prefix = str(hex(key)[2:]+ 'L')
    chars = string.ascii_letters + 5 * string.digits
    # chars是字符集，且增加数字频次
    length = 16 - len(prefix)
    return prefix + ''.join([random.choice(chars) for i in range(length)])

def get_id(code): # code转id
    code = code.split('L')[0]
    return str(int(code.upper(), 16))

for i in range(1, 1001, 50):
    code = get_code(i)
    key = get_id(code)
    print('{} {}'.format(key, code))
