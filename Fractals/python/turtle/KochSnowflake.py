import turtle


def draw_polygon(sides, length):
    for i in range(sides):
        apple.forward(length)
        apple.right(360.0 / sides)


def draw_spiral(angle, length_start, length_increase, sides):
    for i in range(sides):
        apple.forward(length_start+(i*length_increase))
        apple.right(angle)

def draw_petals(length, number):
    for i in range(number):
        apple.forward(length)
        apple.right(180-(360/number))

def draw_fractal(length, depth):
    if depth==1:
        apple.forward(length)
    else:
        draw_fractal(length, depth-1)

    apple.right(60)

    if depth==1:
        apple.forward(length)
    else:
        draw_fractal(length, depth-1)

    apple.left(120)

    if depth==1:
        apple.forward(length)
    else:
        draw_fractal(length, depth-1)

    apple.right(60)

    if depth==1:
        apple.forward(length)
    else:
        draw_fractal(length, depth-1)

def draw_snowflake(length, depth):
    draw_fractal(length, depth-1)
    apple.left(120)
    draw_fractal(length, depth-1)
    apple.left(120)
    draw_fractal(length, depth-1)

apple = turtle.Turtle()

apple.speed(12)

apple.penup()
apple.goto(-300, -200)
apple.pendown()
draw_snowflake(7, 5)

turtle.exitonclick()