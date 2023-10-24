import turtle
from turtle import *
rang = ["red","blue","green","purple"]
t = turtle.Pen()
for x in range(100):
    t.speed(200)
    t.pencolor(rang[x%4])
    t.circle(150-x)
    t.left(91)
    # pensize(x)
    print(x)
done()