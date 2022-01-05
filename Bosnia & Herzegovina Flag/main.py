import turtle
turtle.bgcolor("white")


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


def drawTriangle(x, y, perpendicular, hypotenuse, base, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(perpendicular)
    turtle.right(135)
    turtle.forward(hypotenuse)
    turtle.right(135)
    turtle.forward(base)
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


drawFillRectangle(-230, 125, 280, 500, "#001589")
drawTriangle(175, 125, 280, 395.3, 300, "yellow")
drawStar(-160, 130, "white", 45)
drawStar(-125, 95, "white", 45)
drawStar(-90, 60, "white", 45)
drawStar(-55, 25, "white", 45)
drawStar(-20, -10, "white", 45)
drawStar(15, -45, "white", 45)
drawStar(50, -80, "white", 45)
drawStar(85, -115, "white", 45)
drawStar(120, -150, "white", 45)

turtle.hideturtle()
turtle.done()
