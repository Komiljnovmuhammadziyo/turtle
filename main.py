import turtle
from turtle import *
t = turtle.Pen()
for x in range(200):
    t.pensize(20)
    t.speed(30000)
    t.forward(x)
    t.right(91)
    t.color("red")
    t.forward(x)
    t.right(93)
    t.color("blue")
    t.forward(x)
    t.right(91)
    t.color("purple")
    t.forward(200)
done()


