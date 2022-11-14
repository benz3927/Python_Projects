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
    

def color_scanner(image):
    totals = []
    # go through image pixel by pixel, domaninant,
    
    # color dominance
    lbls = ['red','blue','green']
    clrs = ['red','blue','green']
    plt.pie(totals, explode = None, label = lbs, colors = clrs)
    plt.show()


def impressionist(draw, image):
    for index in range(999999):
        x = randint(0,image.width-1)
        y = randint(0, image.height-1)
        (r,g,b) = image.getpixel((x,y))
        circle(draw,(x,y),5,(r,g,b,200))
        
        
def black_and_white(draw, image):
    for x in range(image.width):
        for y in range(image.height):
            (r,g,b) = image.getpixel((x, y))
            if r + g + b > 384:
                r = r + 256
                g = g + 256
                b = b + 256
                
            else:
                r = r - 256
                g = g - 256  
                b = b - 256
                image.putpixel((x, y), (r, g, b))
        

def main():
    
    start_time = time.time()
    default = Image.open("Federer.png")

## we make it so that the user can put an image of choice in, but set default to Federer
    default
    image_name = input('enter the name of your image file')
    user_image = Image.open(image_name)
    
    
    canvas = Image.new("RGB", (user_image.width, user_image.height))
    draw = ImageDraw.Draw(canvas, "RGBA")

#     draw.ellipse((100, 200, 300, 400), fill = (200, 200, 0,150))
#     draw.ellipse((200, 100, 450, 350), fill = (200, 50, 150, 200))
    
    
#     circle(draw, (200, 300), 100, (200, 200, 0,150))
#     circle(draw, (325, 225), 125, (200, 50, 150,200))
#     draw.rectangle((0, 0, 500, 250), fill = (0, 100, 100))
    
    
    impressionist(draw,default)
#     black_and_white(draw,default)
    canvas.show()
    end_time = time.time()
    print("elapsed time:", end_time - start_time)
    user_image.show()
    default = default.convert('L')
    default.show()
    


    


    #canvas = Image.new("RGB", (500, 500))
    
    #canvas.show()
main()
