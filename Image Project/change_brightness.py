def change_brightness(image):
    answer = int(input("Type in a number between -256 and 256 to make the image darker or brighter respectively! \n"))
    for x in range(image.width):
        for y in range(image.height):
                (r,g,b) = image.getpixel((x, y))
                r = r + answer
                g = g + answer
                b = b + answer
                image.putpixel((x, y), (r, g, b))