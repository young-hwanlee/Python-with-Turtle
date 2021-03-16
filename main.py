# [1. Introduction]
# https://colab.research.google.com/drive/14EIZJLH2_NNi8QQxtqvgB6CgHqrLPkUa?authuser=1#scrollTo=hp30GdAciSbk
# --------------------------------



# [2. 입출력과 변수]
# https://colab.research.google.com/drive/14EIZJLH2_NNi8QQxtqvgB6CgHqrLPkUa?authuser=1#scrollTo=hp30GdAciSbk
# --------------------------------



# # [3. Turtle Graphics]
# # Import turtle package
# import turtle

# turtle.circle(100)
# turtle.circle(-100)
# --------------------------------



# [4. if condition (조건문)]
# num = 10
# num = -10

# if num > 0:
#     print("Positive")
#     print("Done!")
# 
# print("Done!")

# if num > 0:
#     print("Positive")
# else:
#     print("Negative")
# 
# print("Done!")

# num = 0
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# print("Done")

# # [if example]
# # grade A, B, C, D
# # score = 90
# # score = 75
# score = 30

# # >, >=, <, <=, ==, ...
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("D")
# --------------------------------



# [5. Loop]
# count = 0
# while count < 4:
#     print("Run", count)
#     count = count + 1

# count = 1
# while count <= 4:
#     print("Run", count)
#     count = count + 1
# --------------------------------



# [6. Nested if/Loop]
# # [Nested if]
# # num = 10
# num = 7
# 
# if num > 0:
#     print("Positive")
#     if num == 7:
#         print("Lucky!")
# else:
#     print("Negative")

# # num = 7
# num = 8
# 
# if num > 0:
#     print("Positive")
#     if num == 7:
#         print("Lucky!")
#    
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# 
# else:
#     print("Negative")



# # [Nested while loop]
# # y = 2
# # x = 1
# # while x <= 9:
# #     print("2", "*", x, "=", 2 * x)
# #     x = x + 1
# 
# y = 2
# while y <= 9:
#     x = 1
#     while x <= 9:
#         print(y, "*", x, "=", y * x)
#         x = x + 1
#     # print("\n")
#     print("----------")
#     y = y + 1
# --------------------------------



# [7. For Loop]
# # [Basic loop in ascending order]
# i = 0
# while i < 4:
#     print("while run", i)
#     i = i + 1
# 
# for i in range(0, 4, 1):
#     print("for run", i)

# for i in range(1, 10, 1):
#     print("for run", i)

# for i in range(1, 10, 2):
#     print("for run", i)

# for i in range(0, 10, 1):
#     print("for run", i)

# for i in range(10):
#     print("for run", i)

# # [Loop in descending order]
# for i in range(10, 0, -1):
#     print("for run", i)

# for i in range(10, -1, -1):
#     print("for run", i)

# for i in range(9, -1, -1):
#     print("for run", i)

# for i in range(9, -1, -2):
#     print("for run", i)

# --------------------------------



# [8. for nested Loop]
# # [Draw dots]
# import turtle

# # for y in range(0, 200, 20):
# #     for x in range(0, 200, 20):
# #         turtle.up()
# #         turtle.goto(x, y)
# #         turtle.down()
# #         if x == y:
# #             turtle.color("red")
# #         else:
# #             turtle.color("black")
# #         turtle.dot(5)
# 
# # for y in range(0, 200, 20):
# #     for x in range(0, 200, 20):
# #         turtle.up()
# #         turtle.goto(x, y)
# #         turtle.down()
# #         if x == y:
# #             turtle.color("red")
# #         elif x + y == 180:
# #             turtle.color("blue")
# #         else:
# #             turtle.color("black")
# #         turtle.dot(5)
# 
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
#         turtle.dot(x/40 + y/40 + 1)



# # [Draw dots like a shape of right triangle]
# import turtle
# 
# # for y in range(10):
# #     for x in range(y):
# #         r_x = x * 20
# #         r_y = y * 20      
# #         turtle.up()
# #         turtle.goto(r_x, r_y)
# #         turtle.down()
# #         turtle.dot(5)
# 
# for y in range(10):
#     for x in range(y, 10):
#         r_x = x * 20
#         r_y = y * 20
#         turtle.up()
#         turtle.goto(r_x, r_y)
#         turtle.down()
#         turtle.dot(5)



# # [Draw dots like a shape of equilateral triangle]
# import turtle
# 
# # for y in range(10):
# #     for x in range(y, 10):
# #         x_coor = x * 20 - (y * 20)
# #         y_coor = y * 20
# #         turtle.up()
# #         turtle.goto(x_coor, y_coor)
# #         turtle.down()
# #         turtle.dot(5)
# 
# for y in range(10):
#     for x in range(y, 10):
#         x_coor = x * 20 - (y * 10)
#         y_coor = y * 20
#         # print(x_coor, y_coor)
#         turtle.up()
#         turtle.goto(x_coor, y_coor)
#         turtle.down()
#         turtle.dot(5)



# # [Draw circles]
# import turtle
# 
# # for i in range(10):
# #     turtle.circle(i*10)
# 
# # for i in range(10):
# #     turtle.up()
# #     turtle.goto(0, -i*10)
# #     turtle.down()
# #     turtle.circle(i*10)
# 
# for i in range(10, 0, -1):
#     turtle.up()
#     turtle.goto(0, -i*10)
#     turtle.down()
#     if i % 2 == 0:
#         turtle.color("red", "red")      # (drawing color, filling color)
#     else:
#         turtle.color("blue", "blue")
#     turtle.begin_fill()
#     turtle.circle(i*10)
#     turtle.end_fill()
# --------------------------------



# [9. python LIST!]
# [10명 학생들의 점수 기록]
# 각각 변수 vs list

# s0 = 99
# s1 = 100
# s2 = 90

# grade = [90, 100, 80, 70, 60]
# print(grade)
# print(grade[0])
# print(grade[2])
# # print(grade[5])

# grade = [90, 100, 20, 44, 80, 70, 60]
# print("len", len(grade))

# grade = [90, 100, 20, 44, 80, 90, 70, 60]
# print(grade[0])
# print(grade[len(grade) - 1])
# print(grade[len(grade) - 2])
# 
# print(grade[-1])
# print(grade[-2])
# 
# print("len", len(grade))

# grade = [90, 44, 80, 90, 70, 60]
# # print(grade[-1])
# # print(grade[-2])
# 
# print(grade)
# 
# grade[0] = 100
# print(grade)
# 
# grade.sort()
# print(grade)
# 
# print("min", grade[0])
# print("max", grade[-1])

# grade = [90, 44, 80, 90, 70, 60, 100, 10]
# grade.sort()
# print("min", grade[0])
# print("max", grade[-1])

# grade = [[90, 21, 84], [90, 22, 84], [90, 21, 84]]
# print(grade[0])
# print(grade[1])
# 
# x = grade[0]
# print(x[1])
# print(grade[0][1])
# 
# print(grade[2][2])
# print(grade[2][0])
# --------------------------------



# [10. for+list and break&continue]
# grade = [90, 100, 20, 30, 78]
# 
# # for i in range(len(grade)):
# #     print(i, grade[i])
# 
# for score in grade:
#     print(score)

# grade = [99, 100, 89, 30, 78]
# 
# for i in range(len(grade)):
#     # if grade[i] == 99:
#     #     grade[i] = grade[i] + 1
# 
#     if grade[i] % 10 == 9:
#         grade[i] = grade[i] + 1
# 
# print(grade)

# grade = [99, 100, 89, 30, 79]
# 
# for i in range(len(grade)):
#     if grade[i] % 10 == 9:
#         grade[i] = grade[i] + 1
# 
# print(grade)

# grade = [99, 100, 89, 30, 79, 77]
# 
# for i in range(len(grade)):
#     if grade[i] % 10 == 9:
#         grade[i] = grade[i] + 1
# 
#     if grade[i] == 77:
#         grade[i] = grade[i] + 5
# print(grade)

grade = [99, 88, 0, 100, 89, 30, 79, 0, 77]

for i in range(len(grade)):
    # if grade[i] == 0:
    #     break

    if grade[i] == 0:
        continue
    
    print(i, grade[i])