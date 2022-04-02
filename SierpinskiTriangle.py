import turtle
import math
import random
import time

#Initialize Turtle
s = turtle.getscreen()
turtle.title("Sierpinski Triangle")
bunsen = turtle.hideturtle()
bunsen = turtle.Turtle()
bunsen.hideturtle()

#Inputs
trilen = 500
firstpoint = (0,300)
repeat = 5000
bunsen.speed(10)

#Coordinate set up
bottomrightx = trilen/2 #250
midlen = math.sqrt((trilen**2) - (bottomrightx**2))
bottomrighty = firstpoint[1] - midlen #-133

points = {}
points[1] = (0,300)
points[2] = (bottomrightx,bottomrighty)
points[3] = (-bottomrightx,bottomrighty)
current = points[3]

#Drawing starting triangle
bunsen.penup()
bunsen.goto(points[1])
bunsen.dot(8)
bunsen.fd(25)
bunsen.write('A', font=("Arial", 16))
bunsen.goto(points[1])
bunsen.goto(points[2])
bunsen.dot(8)
bunsen.fd(25)
bunsen.write('B', font=("Arial", 16))
bunsen.goto(points[2])
bunsen.goto(points[3])
bunsen.dot(8)
bunsen.bk(25)
bunsen.write('C', font=("Arial", 16))
bunsen.goto(points[3])
bunsen.dot(8)

#Set up function
while repeat > 0:
    rand = random.randint(1, 3)
    target = points[rand]
    nextx = (target[0] + current[0])/2
    nexty = (target[1] + current[1])/2
    next = [nextx, nexty]
    bunsen.goto(next)
    bunsen.dot(8)
    current = next
    repeat -= 1

bunsen.goto(300,300)
bunsen.write('n = ' + str(repeat), font=('Arial',16,'bold'))

#End turtle
turtle.done()

