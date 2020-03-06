import turtle
win=turtle.Screen()
pen=turtle.Turtle()
for i in range(360):
    pen.color('red')
    pen.forward(i)
    pen.right(i)

