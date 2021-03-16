import turtle

# # [Draw dots]
# y = 0
# while y < 200:
#     x = 0
#     while x < 200:
#         turtle.up()
#         turtle.goto(x, y)
#         turtle.down()
#         turtle.dot(5)
#         x = x + 20
#     y = y + 20



# # [Draw dots increasing along the x-axis]
# y = 0
# while y < 200:
#     x = 0
#     while x < 200:
#         turtle.up()
#         turtle.goto(x, y)
#         turtle.down()
#         turtle.dot(x/20 + 1)
#         x = x + 20
#     y = y + 20



# # [Draw dots increasing along both the x-axis & y-axis]
# y = 0
# while y < 200:
#     x = 0
#     while x < 200:
#         turtle.up()
#         turtle.goto(x, y)
#         turtle.down()
#         turtle.dot(y/40 + x/40 + 1)
#         x = x + 20
#     y = y + 20



# # [Draw dots where they are increasing along both the x-axis & y-axis and the diagonals are colored]
# y = 0
# while y < 200:
#     x = 0
#     while x < 200:
#         turtle.up()
#         turtle.goto(x, y)
#         turtle.down()

#         if x == y:
#             turtle.color("red")
#         else:
#             turtle.color("black")
        
#         turtle.dot(y/40 + x/40 + 1)
#         x = x + 20
#     y = y + 20



# # [Draw dots where they are increasing along both the x-axis & y-axis and the diagonals are colored]
y = 0
while y < 200:
    x = 0
    while x < 200:
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

        if x == y:
            turtle.color("red")
        elif x + y == 180:
            turtle.color("blue")
        else:
            turtle.color("black")
        
        turtle.dot(y/40 + x/40 + 1)
        x = x + 20
    y = y + 20