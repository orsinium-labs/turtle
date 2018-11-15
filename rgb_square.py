import turtle

X_START, X_END = -400, 400
Y_START, Y_END = 400, -400

X_PATH = X_END - X_START
Y_PATH = Y_START - Y_END

turtle.speed('fastest')
turtle.penup()
turtle.setx(X_START)
turtle.sety(Y_START)
turtle.pendown()


turtle.colormode(255)


def return_to_left():
    turtle.penup()
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(X_PATH)
    turtle.pendown()
    turtle.right(180)


for _step in range(Y_PATH // 3):
    turtle.pencolor(255, 0, 0)
    turtle.forward(X_PATH)
    return_to_left()

    turtle.pencolor(0, 255, 0)
    turtle.forward(X_PATH)
    return_to_left()

    turtle.pencolor(0, 0, 255)
    turtle.forward(X_PATH)
    return_to_left()

input()
