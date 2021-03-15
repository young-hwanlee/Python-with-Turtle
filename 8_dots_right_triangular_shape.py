# [Draw dots like a shape of right triangle]
import turtle

# for y in range(10):
#     for x in range(y):
#         r_x = x * 20
#         r_y = y * 20      
#         turtle.up()
#         turtle.goto(r_x, r_y)
#         turtle.down()
#         turtle.dot(5)

for y in range(10):
    for x in range(y, 10):
        r_x = x * 20
        r_y = y * 20
        turtle.up()
        turtle.goto(r_x, r_y)
        turtle.down()
        turtle.dot(5)