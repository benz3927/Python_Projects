"""
Images and Timing
"""
import time
from PIL import Image, ImageDraw
from random import *

def main():
    my_image = Image.open("sea.jpg")
    canvas = Image.new("RGB", (my_image.width, my_image.height))
    draw = ImageDraw.Draw(canvas, "RGBA")
    fiveK_pixels(draw, my_image)
    canvas.show()
    end_time = time.time()
    print("elapsed time:", end_time - start_time)
def fiveK_pixels(draw, image):
    for index in range(100000):
        x = randint(0, image.width-1)
        y = randint(0, image.height-1)
        (r, g, b) = image.getpixel((x,y))
        circle(draw, (x+3,y+5), 10, (r+5,g+20,b*2, 200))
        
def circle(draw, center, radius, color):
    draw.ellipse((center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius), fill = color)
    pass
    

if __name__ == "__main__":
    main()
