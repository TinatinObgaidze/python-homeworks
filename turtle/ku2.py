import turtle
turtle.shape("turtle")
turtle.color("orange")
for i in range(0, 18):
    turtle.forward(100)
    turtle.left(100)
    turtle.backward(100)
    turtle.forward(100)
    turtle.right(100)
    turtle.backward(120)
    turtle.forward(60)
    turtle.left(20)

turtle.exitonclick()