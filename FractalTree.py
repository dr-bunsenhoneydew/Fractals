import turtle

#Initialize Turtle
s = turtle.getscreen()
turtle.title("Sierpinski Triangle")
bunsen = turtle.hideturtle()
bunsen = turtle.Turtle()
bunsen.hideturtle()
bunsen.speed(10)
bunsen.pensize(3)
bunsen.lt(90)
bunsen.penup()
bunsen.goto(0,-300)
bunsen.pendown()


angle = 30

def fractalTree(size, level):
    if level > 0:
        turtle.colormode(255)
        bunsen.pencolor(0, 255/level, 0)
        bunsen.fd(size)
        bunsen.rt(angle)
        y(.8 * size, level - 1)
        bunsen.pencolor(0, 255/level, 0)
        bunsen.lt(2 * angle)
        y(.8 * size, level - 1)
        bunsen.pencolor(0, 255/level, 0)
        bunsen.rt(angle)
        bunsen.fd(-size)

fractalTree(150, 12)
