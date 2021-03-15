# Import turtle package
import turtle

# Set the fill color to red
# turtle.fillcolor('red')
turtle.fillcolor('blue')

# Start filling the color
turtle.begin_fill()

# Draw the left line
turtle.left(140)
turtle.forward(113)

# Draw the left curve
turtle.circle(-57, 200)
turtle.left(120)

# Draw the right curve
turtle.circle(-57, 200)

# Draw the right line
turtle.forward(112)

# Ending the filling of the color
turtle.end_fill()

# Move turtle to air
turtle.up()

# Move turtle to a given position
turtle.goto(-60, 95)

# Move the turtle to the ground
turtle.down()

# Set the text color to lightgreen
turtle.color('lightgreen')

# Write the specified text in
# specified font style and size
turtle.write("I Love YOU", font=("Verdana", 15, "bold"))

# To hide turtle
turtle.ht()