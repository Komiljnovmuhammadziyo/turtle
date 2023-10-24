
import turtle
import time
trtl=turtle.Turtle()
trtl.pencolor('red')     #making colour of the pen red
trtl.pensize(5)     #choosing the size of pen nib
#trtl.speed(1)     #choosing the speed of drawing
trtl.shape('turtle')    #choosing the shape of pen n
n=3    #starting for a triangle
shapes=['Triangle','Square','Pentagon','Hexagon','Heptagon','Octagon','Nonagon','Decagon']
while n<11: #    limiting to a decagon
        trtl.clear()
        for i in range(n):     # for loop to minimize the same lines of codes being written
            trtl.pencolor('red')
            trtl.forward(60)     #top line
            trtl.right(360/n)
        n=n+1
        trtl.penup()
        trtl.home()
        trtl.pendown()
        trtl.penup()
        trtl.home()    #moving the turtle to make the animation more centric
        trtl.pendown()
        trtl.ht()
        time.sleep(1)
        trtl.st()