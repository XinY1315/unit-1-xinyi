import turtle
from turtle import *
t = Turtle()


""" sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90) """

""" def triangle(x,y):
    for i in range(3):
        t.forward(100)
        t.left(120)
triangle(100,100)
 """
""" sidelength = 5
rotate = 5
def square(x,y):
    for i in range(240):
        t.forward(x)
        t.left(y)
square(5,10) """
#this made a circle so let that sink in

""" def sixtysquare(x,y):
    for i in range(60):
        t.right(5)
        for i in range(4):
            t.forward(100)
            t.left(90)
sixtysquare(100, 90)  """
""" 
sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90) """

""" def doublesquares(iRange):
    length = 20
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doublesquares(5) """


""" def addsquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addsquares(5) """

""" def sixtysquare(iRange):
    length = 5
    for i in range(60):
        t.right(5)
        length += 5
        for i in range(4):
            t.forward(length)
            t.left(90)
sixtysquare(60) """

sidelength = 100
rotate = 65
def star(iRange):
    for i in range(6):
        t.forward(100)
        t.right(100)
star(6)