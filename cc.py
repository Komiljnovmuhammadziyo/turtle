import turtle as t
t.speed(0)
t.pensize(2)
rang = ["red","blue","green","purple","black"]
t.penup()
t.goto(300,-200)
t.pendown()
for i in range(200):
    t.pencolor(rang[i%5])
    t.right(15)
    t.forward(90)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(124)
    t.left(120)
    t.forward(90)
    t.right(120)
    t.forward(120)
    t.right(90)
    t.forward(90)
    t.right(120)
    t.forward(90)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(124)
    t.right(90)
    t.forward(120)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(124)
    t.left(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(120)
    t.forward(120)
    t.right(120)
    t.forward(120)
    t.forward(120)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(124)
    t.left(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(190)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.pendown()
    t.right(90)
    t.forward(124)
    t.right(90)
    t.forward(120)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(124)
    t.left(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(124)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)

t.exitonclick()