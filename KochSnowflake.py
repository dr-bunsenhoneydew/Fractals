# Python program to print complete Koch Curve.
import turtle

s = turtle.getscreen()
turtle.title("Koch Snowflake")
bunsen = turtle.hideturtle()
bunsen = turtle.Turtle()
bunsen.hideturtle()
bunsen.speed(0)
bunsen.color('sky blue','white')

# function to create koch snowflake or koch curve
def kochSnowflake(lengthSide, levels):
    if levels == 0:
        bunsen.forward(lengthSide)
        return
    lengthSide /= 3.0
    kochSnowflake(lengthSide, levels-1)
    bunsen.left(60)
    kochSnowflake(lengthSide, levels-1)
    bunsen.right(120)
    kochSnowflake(lengthSide, levels-1)
    bunsen.left(60)
    kochSnowflake(lengthSide, levels-1)

def runSnowflake(lengthSide, levels):
    bunsen.penup()
    bunsen.backward(lengthSide/2)
    bunsen.left(90)
    bunsen.forward(lengthSide/4)
    bunsen.right(90)
    bunsen.pendown()
    for i in range(3):
        kochSnowflake(lengthSide, levels)
        bunsen.right(120)

runSnowflake(500,5)


