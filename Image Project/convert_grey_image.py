from PIL import Image

def main():
    hamilton = Image.open("hamilton.jpg")
    hamilton = hamilton.convert('M') # convert image to black and white
    hamilton.show()
main()