import turtle
from turtle import *
rang = ["red","blue","green","purple","black"]
t = turtle.Pen()
qadam = 0
while qadam <10:
    t.pencolor(rang[qadam%5])
    for i in range(5):
        t.speed(200)
        t.pensize(2)
        t.forward(200)
        t.right(144)
    t.right(45)
    qadam +=1
done()