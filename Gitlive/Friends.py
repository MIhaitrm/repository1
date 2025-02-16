import turtle

def draw_shape(sides):
    for _ in range(sides):
        turtle.forward(100)
        turtle.left(360 / sides)

sides = int(input("Enter the number of sides for the shape: "))
draw_shape(sides)
turtle.done()

