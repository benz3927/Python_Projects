# 3 images

# arts, input a picture

# ask user to input 3 colors shades of that color

# art gallery

# filter


# black and white

# brightness


from PIL import Image, ImageDraw
from random import *
import time

from matplotlib import pyplot as plt

def circle(draw, center, radius, color):
    draw.ellipse((center[0]-radius,center[1]-radius,center[0]+radius,center[1]+radius),fill = color)


def impressionist(draw, image):
    for index in range(999999):
        x = randint(0,image.width-1)
        y = randint(0, image.height-1)
        (r,g,b) = image.getpixel((x,y))
        circle(draw,(x,y),5,(r,g,b,200))


def color_totals(image):
    colors = {"red": 0,
              "green": 0,
              "blue": 0}
    for x in range(image.width):
        for y in range(image.height):
            (r,g,b) = image.getpixel((x,y))
            if r>g and r>b:
                colors["red"] = colors["red"] + 1
            elif g>r and g>b:
                colors["green"] = colors["green"] + 1
            elif b>r and b>g:
                colors["blue"] = colors["blue"] + 1
            else:
                continue
    return colors

def blues(draw, image, canvas):
    for index in range(100000):
        x = randint(0, image.width-1)
        y = randint(0, image.height-1)
        (r, g, b) = image.getpixel((x,y))
        circle(draw, (x,y), 5, (r+5,g+20,b*2, 200))
    new_image = canvas.copy()
    return new_image

def oranges(draw, image, canvas):
    for index in range(100000):
        x = randint(0, image.width-1)
        y = randint(0, image.height-1)
        (r, g, b) = image.getpixel((x,y))
        circle(draw, (x,y), 5, (r*2,g+10,b-2, 200))
    new_image = canvas.copy()
    return new_image
        
def purples(draw, image, canvas):
    for index in range(100000):
        x = randint(0, image.width-1)
        y = randint(0, image.height-1)
        (r, g, b) = image.getpixel((x,y))
        circle(draw, (x,y), 5, (r,g+35,b*3, 200))
    new_image = canvas.copy()
    return new_image
        

def main():
    
    start_time = time.time()
    default = Image.open("Federer.png")

## we make it so that the user can put an image of choice in, but set default to Federer
    default
    image_name = input('enter the name of your image file: ')
    user_image = Image.open(image_name)
    
    print(color_totals(user_image))
    
    canvas = Image.new("RGB", (user_image.width, user_image.height))
    draw = ImageDraw.Draw(canvas, "RGBA")

#     draw.ellipse((100, 200, 300, 400), fill = (200, 200, 0,150))
#     draw.ellipse((200, 100, 450, 350), fill = (200, 50, 150, 200))
    
    
#     circle(draw, (200, 300), 100, (200, 200, 0,150))
#     circle(draw, (325, 225), 125, (200, 50, 150,200))
#     draw.rectangle((0, 0, 500, 250), fill = (0, 100, 100))

# Back and white high resolution
#     default = default.convert('L')
#     default.show()
    
# purples
    
    purple = purples(draw, user_image, canvas) 
    
    
# Cool Hues Saturated blue green
    blue = blues(draw, user_image, canvas)

# Warm Hues Saturated red orange
    orange = oranges(draw, user_image, canvas)

# black_and_white(draw,default)
    purple.show()
    blue.show()
    orange.show()
    end_time = time.time()
    print("elapsed time:", end_time - start_time)
    
    


    


    #canvas = Image.new("RGB", (500, 500))
    
#     canvas.show()
main()
