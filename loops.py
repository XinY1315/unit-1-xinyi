import turtle
from turtle import *
t = Turtle()

#i is an incrementor
# -= and += means subtract or add what's on the right to the og


sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90)

def triangle(x,y):
    for i in range(3):