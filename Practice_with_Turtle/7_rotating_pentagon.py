import turtle

n = 5
m = 8
for _ in range(m):
    for _ in range(n):
        turtle.forward(100)
        turtle.right(360/n)
    turtle.right(360/m)