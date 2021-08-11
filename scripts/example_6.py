import turtle

#Screen configutarion
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
screen.bgcolor("red")
screen.title("Turtle Program - Jhon Galindo")

#Create a turtle
t = turtle.Turtle()

#Turtle configuration
t.pensize(10)
t.pencolor("white")
t.shapesize(3,3,3)
t.fillcolor("blue")
t.shape("turtle")

#Move turtle
t.speed(1)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)

turtle.done()