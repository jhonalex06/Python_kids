import turtle
 
t = turtle.Turtle()

#Screen Configuration
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

#Turtle configuration
t.pensize(10)
t.pencolor("white")
t.shapesize(3,3,3)
t.fillcolor("blue")
t.shape("turtle")

#blue circle
t.penup()
t.pencolor("blue")
t.goto(0, 0)
t.pendown()
t.circle(100)

#black circle
t.penup()
t.pencolor("black")
t.goto(220, 0)
t.pendown()
t.circle(100)

#red circle
t.penup()
t.pencolor("red")
t.goto(440, 0)
t.pendown()
t.circle(100)

#yellow circle
t.penup()
t.pencolor("yellow")
t.goto(110, -100)
t.pendown()
t.circle(100)

#green circle
t.penup()
t.pencolor("green")
t.goto(330, -100)
t.pendown()
t.circle(100)
 
turtle.done()