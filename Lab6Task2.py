# CST 205
# Charlie Nguyen
# Oct 8, 2020
# This program demonstrates chroma key by placing an otter on the beach

import math
# from numpy import mean
from PIL import Image

person = Image.open('images/otter2.jpg')
scene = Image.open('images/beach.jpg')
green = person.getpixel((10, 50))

w = min(person.width, scene.width)
h = min(person.height, scene.width)
scene = scene.resize((person.width, person.height))


def distance(color_1, color_2):
    r_diff = math.pow((color_1[0] - color_2[0]), 2)
    g_diff = math.pow((color_1[1] - color_2[1]), 2)
    b_diff = math.pow((color_1[2] - color_2[2]), 2)
    return math.sqrt(r_diff + g_diff + b_diff)


def chromakey(src, bg):
    for x in range(src.width):
        for y in range(src.height):
            cur_pixel = src.getpixel((x, y))
            if distance(cur_pixel, green) < 160:
                src.putpixel((x, y), bg.getpixel((x, y)))
    src.save('chromakeyOtter.jpg')
    src.show()


chromakey(person, scene)