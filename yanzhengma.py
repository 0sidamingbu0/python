import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机码 默认长度=1
def random_code(lenght=1):
    code = ''
    for char in range(lenght):
        code += chr(random.randint(65, 90))
    return code


# 随机颜色 默认颜色范围【1，255】
def random_color(s=1, e=255):
    return (random.randint(s, e), random.randint(s, e), random.randint(s, e))


# 生成验证码图片
# length 验证码长度
# width 图片宽度
# height 图片高度
# 返回验证码和图片
lenght = 8
width = 320
height = 40
# 创建Image对象
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('arial.ttf', 32)
# 创建Draw对象

# 随机颜色填充每个像素
for i in range(1,100):
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=random_color(128, 254))
    # 验证码
    code = random_code(lenght)
    # 随机颜色验证码写到图片上
    for t in range(lenght):
        draw.text((40 * t + 5, 5), code[t], font=font, fill=random_color(0, 127))
    # 模糊滤镜
    image = image.filter(ImageFilter.BLUR)
    #image.show()
    image.save(code +".jpg")
    print(code)
