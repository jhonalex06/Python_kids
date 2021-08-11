import turtle

#Screen configutarion
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
screen.bgcolor("red")

#Create a turtle
t = turtle.Turtle()

#Turtle configuration
t.pensize(10)
t.pencolor("white")

#Move turtle
t.speed(1)
t.forward(400)

turtle.done()