# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
# 将同一目录下的img.jpg，处理后保存为output.jpg

from PIL import Image, ImageFont, ImageDraw

im = Image.open("./img.jpg")
draw = ImageDraw.Draw(im)

content = input('请键入文本')

fontpath = "~/library/fonts/CONSOLA.TTF"
fontsize = (int)(min(im.size) / 4)
font = ImageFont.truetype(fontpath, fontsize)
draw.text((im.size[0] - fontsize, 0), content, font = font, fill = (255, 0, 0)) 
im.save('./output.jpg', "jpeg")
