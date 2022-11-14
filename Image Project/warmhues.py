"""
Images and Timing
"""
import time
from PIL import Image, ImageDraw
from random import *



def main():

    
    #Problems 1-4
    start_time = time.time()
    
    
    #Problem 1
    #draw.ellipse((100, 200, 300, 400), fill = (200, 200, 0))
    #draw.ellipse((200, 100, 450, 350), fill = (200, 50, 150))
    #Problem 2/3
    #draw.ellipse((100, 200, 300, 400), fill = (200, 200, 0, 150))
    #draw.ellipse((200, 100, 450, 350), fill = (200, 50, 150, 200))
    #Problem 4 (Will work on later)
    #draw.rectangle((0, 0, 500, 250), fill = (0, 100, 100))
    #draw.ellipse((100, 100, 200, 200), fill = (200, 50, 150, 200))
    #Problem 5
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
        circle(draw, (x+3,y+5), 10, (r*2,g+10,b-2, 200))

    #canvas.show() (Problems 1-4)
    
    
    """
    Image 2
    """
def circle(draw, center, radius, color):
    draw.ellipse((center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius), fill = color)
    pass
    
    
    
    




if __name__ == "__main__":
    main()
