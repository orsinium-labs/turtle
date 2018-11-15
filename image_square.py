from PIL import Image
import turtle


im = Image.open('input.jpg')
pixels = im.load()

X_PATH, Y_PATH = im.size

X_START, X_END = -400, -400 + Y_PATH
Y_START, Y_END = 400, 400 + X_PATH
STEP = 20


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


def write_pixel(x, y, channel):
    pixel = pixels[x, y]
    pixel = [0 if color == channel else color for color in pixel]
    turtle.pencolor(*pixel)
    turtle.forward(STEP)


for y in range(0, Y_PATH - 3, 3):
    for x in range(0, X_PATH, STEP):
        write_pixel(x, y, 0)
    return_to_left()

    y += 1
    for x in range(0, X_PATH, STEP):
        write_pixel(x, y, 1)
    return_to_left()

    y += 1
    for x in range(0, X_PATH, STEP):
        write_pixel(x, y, 2)
    return_to_left()

input()
