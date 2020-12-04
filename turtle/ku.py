import turtle
turtle.shape("turtle")
turtle.color("green", "black")
turtle.begin_fill()
for i in range(0, 3):
    turtle.right(120)
    turtle.forward(100)
for i in range(0, 3):
    turtle.left(120)
    turtle.forward(100)
turtle.circle(15, 360, 15)
for i in range(0, 3):
    turtle.left(120)
    turtle.backward(100)
for i in range(0, 3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()
turtle.exitonclick()