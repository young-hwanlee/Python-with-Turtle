import turtle

# for i in range(10, 0, -1):
#     if i % 2 == 1:
#         turtle.color("red", "red")
#     else:
#         turtle.color("blue", "blue")
# 
#     turtle.up()
#     turtle.goto(0, -i*10)
#     turtle.down()
# 
#     turtle.begin_fill()
#     turtle.circle(i*10)
#     turtle.end_fill()
# 
#     turtle.ht()



# color_list = ["blue", "red", "forest green"]
color_list = ["royal blue", "green yellow", "dark orange", "red", "blue", "indigo", "orange", "yellow", "orange red", "magenta"]

for i in range(9, -1, -1):
    turtle.up()
    turtle.goto(0, -i*10)
    turtle.down()

    turtle.color(color_list[i], color_list[i])
    turtle.begin_fill()
    turtle.circle(i*10)
    turtle.end_fill()

    turtle.ht()