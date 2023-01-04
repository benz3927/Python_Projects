# Import all elements of the turtle library:
from turtle import *
from random import *
import math



# Set up the graphics window:

screen = Screen()
screen.setup(1000, 1200)
screen.bgcolor("midnight blue")

# Create a turtle object and set some of its attributes:
dude = Turtle()
dude.shape("turtle")
dude.resizemode("auto")
dude.width(1.25)
dude.pencolor("gold")
dude.speed(0)


### Once the pandemic is over, and I become a full-fledged adult, I have enough money, I hope to one day visit Europe and Paris.
### This project idea was inspired because I was in my dorm at night, and it was dark outside, and I was thinking of doing a landscape
### but landscapes are hard and my drawing/blending skills, are limited to computer values and my limited understanding of thonny,
### So I thought midnight blue could be a beautiful background for the Eiffel Tower in a night-time scene.

screen.bgcolor("midnight blue")

# define functions for each portion of the building
# use if statements for user input phrase
# loop cross hatches



def reset_top_of_page():
    dude.penup()
    x = 0
    y= 200
    dude.goto(x,y)
    dude.pendown()



def draw_right_leg():
    for index in range(1,120):
        dude.dot()
        dude.forward(index*0.02)
        dude.left(90)
        dude.forward(2 * (math.log(index/200)))
        dude.dot()
        dude.right(90)
        if index == 50:
            print(f"right top platform {dude.pos()} coordinates")
        if index == 73:
            print(f"right platform 1 {dude.pos()} coordinates")
        if index == 83:
            print(f"right platform 2 {dude.pos()} coordinates")
    


def draw_left_leg():
    for index in range(1,120):
        dude.dot()
        dude.forward(index*0.02)
        dude.right(90)
        dude.forward(2 * (math.log((index/200))))
        dude.dot()
        dude.left(90)
        if index == 73:
            print(f"left platform 1 {dude.pos()} coordinates")
        if index == 83:
            print(f"left platform 2 {dude.pos()} coordinates")

# def user input for scene moon and text
    
    


def draw_right_pillar():
    for index in range(1,86):
        dude.dot()
        dude.forward(index*0.02)
        dude.left(90)
        dude.forward(2 * (-0.25 + math.log(index/200)))
        dude.dot()
        dude.right(90)


def draw_left_pillar():
    for index in range(1,86):
        dude.dot()
        dude.forward(index*0.02)
        dude.right(90)
        dude.forward(2 * (- 0.25 +math.log((index/200))))
        dude.dot()
        dude.left(90)

def draw_line(x,y,length):
    dude.penup()
    dude.goto(x,y)
    dude.pendown()
    dude.width(3.5)
    dude.forward(length)
    dude.penup()
    

def moon():
    moon_or_not = input("Would you like a moon or not? y/n")
    if moon_or_not == 'y':
        dude.penup()
        dude.goto(180,200)
        dude.pendown()
        dude.fillcolor('blanchedalmond')
        dude.begin_fill()
        dude.circle(30)
        dude.end_fill()
        dude.penup()
    if moon_or_not == 'n':
        print("k that's fine")

def main():
# Draw legs
    reset_top_of_page()
    draw_right_leg()
    print(dude.pos())
    
    reset_top_of_page()
    dude.right(180)
    draw_left_leg()
    print(dude.pos())
    
    reset_top_of_page()
    dude.right(180)
#Draw pillars
    draw_right_pillar()
    print(dude.pos())
    
    reset_top_of_page()
    dude.right(180)
    draw_left_pillar()
    dude.right(180)
#draw lines

# draw bases
    draw_line(-143,-154, 70)
    draw_line(73,-154, 70)
    
#draw top platform
    draw_line(-25.50,-32.88,50)

# draw platform 1
    draw_line(-54.02,-87.02,108)
# draw platform 2
    draw_line(-69.72,-105.73,140)
# ask user input for moon and words
    moon()
    


main()

# Find position of turtle
# from turtle import *
# import turtle as tur
# def position(event):
#     a, b = event.x, event.y
#     print('{}, {}'.format(a, b))
# 
# ws = tur.getcanvas()
# ws.bind('<Motion>', position)
# tur.done()

# at starting point (x,y)




# draw lines
# x is off because of x,y tracker was wrong
# x= x-513.1, y= y -348

# draw_line(-73.10,-151.68,120)



## Eifel Tower dimensions
### coordinates notes
### starting platform 1
    # L: (-54.02,-87.02)
    # R: (54.02,-87.02)
### starting platform 2
    # L: (-69.72,-105.73)
    # R: (69.72,-105.73)
### bottom arc position - done
    # (73.10,-151.68)
    # (-73.10,-151.68)
###base - done
    # (142.80,-154.95)
    # (-142.80,-154.95)
    # (73.10,-151.68)
    # (-73.10,-151.68)
## another platform

    
#### arc
    
#### fonts







# def message():
#     dude.penup()
#     dude.goto(0,-230)
#     dude.pendown()
#     response = input("Which message would you like on your card: none / 1 / 2 / 3 ?")
#     if response == 'none':
#         print('k!')
#     if response == '1':
#         dude.write()
#     if response == '2':
#         dude.write()
#     if response == '3':
#         dude.write()


dude.hideturtle()






