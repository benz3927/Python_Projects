def red_filter(image):
    """Takes an image, and makes it more red.
    This is a template for many useful functions!"""
    for x in range(image.width):
        #print("Working on column", x) ### To see how long it will take
        for y in range(image.height):
            ## This tuple assignment gets the r, g, and b components
            ## of the pixel's color
            (r,g,b) = image.getpixel((x, y))
            r = r + 140
            image.putpixel((x, y), (r, g, b))
def blue_filter(image):
    """Takes an image, and makes it more red.
    This is a template for many useful functions!"""
    for x in range(image.width):
        #print("Working on column", x) ### To see how long it will take
        for y in range(image.height):
            ## This tuple assignment gets the r, g, and b components
            ## of the pixel's color
            (r,g,b) = image.getpixel((x, y))
            b = b + 140
            image.putpixel((x, y), (r, g, b))
def green_filter(image):
    """Takes an image, and makes it more red.
    This is a template for many useful functions!"""
    for x in range(image.width):
        #print("Working on column", x) ### To see how long it will take
        for y in range(image.height):
            ## This tuple assignment gets the r, g, and b components
            ## of the pixel's color
            (r,g,b) = image.getpixel((x, y))
            g = g + 140
            image.putpixel((x, y), (r, g, b))

            
def black_and_white(image):
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