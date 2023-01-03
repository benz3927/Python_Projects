from PIL import Image, ImageDraw
from random import *
import time


def color_totals(image):
    colors = {red:0,
              green:0,
              blue:0}
    for x in range(image.width):
        for y in range(image.height):
            (r,g,b) = image.getpixel((x,y))
            if r>g and r>b:
                colors[red] = colors[red] + 1
            elif g>r and g>b:
                colors[green] = colors[green] + 1
            elif b>r and b>g:
                colors[blue] = colors[blue] + 1
            else:
                continue
    return colors

default = Image.open("Federer.png")
print(color_totals(default))