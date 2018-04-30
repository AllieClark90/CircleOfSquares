
import turtle

my_turtle = turtle.Turtle()
turtle.speed(100)

#square
def square(length, angle):
    for i in range(4):
        turtle.forward(length)
        turtle.left(angle)

#loops    
for i in range(400):
    square(100, 90)
    turtle.right(28)