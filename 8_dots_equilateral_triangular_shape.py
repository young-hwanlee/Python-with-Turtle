# [Draw dots like a shape of equilateral triangle]
import turtle

# for y in range(10):
#     for x in range(y, 10):
#         x_coor = x * 20 - (y * 20)
#         y_coor = y * 20
#         turtle.up()
#         turtle.goto(x_coor, y_coor)
#         turtle.down()
#         turtle.dot(5)

for y in range(10):
    for x in range(y, 10):
        x_coor = x * 20 - (y * 10)
        y_coor = y * 20
        # print(x_coor, y_coor)
        turtle.up()
        turtle.goto(x_coor, y_coor)
        turtle.down()
        turtle.dot(5)