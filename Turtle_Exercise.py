# Lesson 1 - Turtle
import turtle
george = turtle.Turtle()
george.width(5)
george.speed(3)

# Making a triangle:
george.color("red")
george.forward(100)
george.right(135)
george.forward(140)
george.right(135)
george.forward(100)

# Making a square:
george.penup()
george.forward(150)
george.pendown()

for color_side in ["yellow", "red", "green", "blue"]:
    george.color(color_side)
    george.forward(100)
    george.right(90)

# Let's try a five points star (angle inside - 36 degrees):
george.color("pink")
george.penup()
george.left(90)
george.forward(150)
george.pendown()
for side in range(5):
    george.forward(100)
    george.right(144)

# Eight point star (angle inside: 45):
george.color("darkgreen")
george.penup()
george.right(90)
george.back(150)
george.pendown()
for side in range(8):
    george.forward(100)
    george.right(135)

# Some shapes:

george.color("cyan")

george.penup()
george.back(150)
george.pendown()

for shape in range(6):
    for side in range(6):
        george.forward(40)
        george.right(60)
    george.penup()
    george.forward(15)
    george.pendown()
    george.right(-60)




