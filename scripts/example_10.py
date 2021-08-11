import turtle
t = turtle.Turtle()

#Screen Configuration
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

def draw_leaf(size):
    leaf_points = [[0, 7], [-1.2, 4.4], [-3, 5], [-2, 1],
                   [-4, 3], [-4.3, 1.5], [-7, 2.5], [-5.5, 0],
                   [-7, -1], [-3.3, -3.4], [-4, -5], [-0.2, -4.2],
                   [-0.2, -8], [0.2, -8], [0.2, -4.2], [4, -5],
                   [3.3, -3.4], [7, -1], [5.5, 0], [7, 2.5],
                   [4.3, 1.5], [4, 3], [2, 1], [3, 5],
                   [1.2, 4.4], [0, 7]]
    t.color('red')
    t.begin_fill()
    for (x, y) in leaf_points:
        t.goto(x * size, y * size)
    t.end_fill()


draw_leaf(size=40)
turtle.done() 