# 第 0010 题：使用 Python 生成字母验证码图片。
import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter

def get_chars():
    return [random.choice(string.ascii_letters) for _ in range(4)]

def get_color(Min, Max):
    return (0, random.randint(Min, Max), random.randint(Min, Max))

def get_picture(width, height):
    # 创建画布
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('/Library/Fonts/CONSOLA.TTF', 80)
    draw = ImageDraw.Draw(image)
    # 生成验证码
    code = get_chars()
    for i in range(4):
        draw.text((60 * i + 10, 0), code[i], font = font, fill = get_color(100, 200))
    # 生成噪声
    for i in range(5000):
        draw.point((random.randint(0, width), random.randint(0, height)), fill = get_color(100, 250))
    # 模糊处理
    image = image.filter(ImageFilter.BLUR)

    image.save('code.jpg', 'jpeg')

get_picture(240, 80)
