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