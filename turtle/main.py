import turtle
# 1
turtle.shape("turtle")
turtle.begin_fill()
turtle.color("blue","violet")
for i in range(0, 4):
    turtle.forward(90)
    turtle.left(90)
for i in range(0, 4):
    turtle.backward(90)
    turtle.right(90)
for i in range(0, 4):
    turtle.forward(90)
    turtle.right(90)
for i in range(0, 4):
    turtle.backward(90)
    turtle.left(90)
turtle.end_fill()
turtle.exitonclick()

