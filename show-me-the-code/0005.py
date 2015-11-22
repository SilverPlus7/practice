# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# 形成当前目录下的图片的缩略图，分辨率不超过640 * 1136，保存在output目录下。

import os
from PIL import Image

outpath = './output/'
os.system('mkdir output')

cnt = 0

for i in os.listdir(os.getcwd()):
    postfix = os.path.splitext(i)[1]
    if postfix == '.jpg' or postfix == '.png':
        image = Image.open('./' + i)
        type = 'jpeg' if postfix == 'jpg' else 'png'
        if image.size[0] > 640 or image.size[1] > 1136:
            rate = max(image.size[0] / 640.0, image.size[1] / 1136.0)
        else:
            rate = 1
        image.thumbnail((image.size[0] / rate, image.size[1] / rate))
        image.save(outpath + i, type)
        print('完成第{}张图片，缩放比率{:.2f}'.format(cnt, 1.0 / rate))
        cnt = cnt + 1
