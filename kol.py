import turtle

turtle.speed('fastest')

# making the turtle face upwards
turtle.right(-90)

# angle between the base and branch of the Y tree
angle = 30

# plot a Y tree
def y_tree(size, level):

    if level > 0:
        turtle.colormode(255)

        # splitting the RGB range for green
        # into equal intervals for each level
        # setting the color according
        # to the current level
        turtle.pencolor(0, 255//level, 0)

        # drawing the tree base
        turtle.forward(size)

        turtle.right(angle)

        # recursive calling for right subtree
        y_tree(0.8 * size, level-1)

        turtle.pencolor(0, 255//level, 0)

        turtle.left( 2 * angle )

        # recursive calling for left subtree
        y_tree(0.8 * size, level-1)

        turtle.pencolor(0, 255//level, 0)

        turtle.right(angle)
        turtle.forward(-size)


# tree of size 80 and level 7
y_tree(80, 7)

turtle.done()
