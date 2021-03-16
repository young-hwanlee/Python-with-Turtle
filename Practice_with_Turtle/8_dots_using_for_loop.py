# [Draw dots]
import turtle

# for y in range(0, 200, 20):
#     for x in range(0, 200, 20):
#         turtle.up()
#         turtle.goto(x, y)
#         turtle.down()
#         if x == y:
#             turtle.color("red")
#         else:
#             turtle.color("black")
#         turtle.dot(5)

# for y in range(0, 200, 20):
#     for x in range(0, 200, 20):
#         turtle.up()
#         turtle.goto(x, y)
#         turtle.down()
#         if x == y:
#             turtle.color("red")
#         elif x + y == 180:
#             turtle.color("blue")
#         else:
#             turtle.color("black")
#         turtle.dot(5)

for y in range(0, 200, 20):
    for x in range(0, 200, 20):
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        if x == y:
            turtle.color("red")
        elif x + y == 180:
            turtle.color("blue")
        else:
            turtle.color("black")
        turtle.dot(x/40 + y/40 + 1)