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
turtle.pencolor(255, 0, 0)

for _step in range(Y_PATH):
    turtle.forward(X_PATH)
    turtle.penup()
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)

    turtle.forward(X_PATH)
    turtle.pendown()
    turtle.right(180)

input()
