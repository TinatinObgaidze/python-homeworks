import turtle
turtle.shape("turtle")
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0, 5):
    turtle.forward(100)
    turtle.right(72)
for i in range(0, 5):
    turtle.backward(100)
    turtle.left(72)
for i in range(0, 5):
    turtle.backward(100)
    turtle.right(72)
for i in range(0, 5):
    turtle.forward(100)
    turtle.left(72)
turtle.end_fill()
turtle.color("black")
turtle.begin_fill()
for i in range(0, 3):
    turtle.right(120)
    turtle.forward(100)
for i in range(0, 3):
    turtle.left(120)
    turtle.forward(100)
for i in range(0, 3):
    turtle.left(120)
    turtle.backward(100)
for i in range(0, 3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()