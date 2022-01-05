import turtle
turtle.bgcolor("gray")


def drawFillRectangle(x,y,length,width,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()


def drawCircle(x, y, color, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def drawStar(x, y, color, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for star in range(0, 5):
        turtle.forward(length)
        turtle.right(144)

    turtle.end_fill()


drawFillRectangle(-230, 125, 260, 450, "black")
drawFillRectangle(-230, 125, 60, 450, "blue")
drawFillRectangle(-230, 65, 5, 450, "white")
drawFillRectangle(-230, 60, 130, 450, "red")
drawFillRectangle(-230, -70, 5, 450, "white")
drawFillRectangle(-230, -75, 60, 450, "blue")

drawCircle(-110, -60, "white", 55)
drawStar(-160, 10, "red", 100)

turtle.hideturtle()
turtle.done()