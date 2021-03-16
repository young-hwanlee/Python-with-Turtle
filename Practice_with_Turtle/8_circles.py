# [Draw circles]
import turtle

# for i in range(10):
#     turtle.circle(i*10)

# for i in range(10):
#     turtle.up()
#     turtle.goto(0, -i*10)
#     turtle.down()
#     turtle.circle(i*10)

for i in range(10, 0, -1):
    turtle.up()
    turtle.goto(0, -i*10)
    turtle.down()
    if i % 2 == 0:
        turtle.color("red", "red")      # (drawing color, filling color)
    else:
        turtle.color("blue", "blue")
    turtle.begin_fill()
    turtle.circle(i*10)
    turtle.end_fill()