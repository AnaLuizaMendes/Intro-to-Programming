# Rainbow time
import turtle

# Call and initiate the Turtle
ray = turtle.Turtle()
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

ray.speed(3)
ray.width(5)


for rainbow_color in rainbow:
    # Change the color of turtle for each interaction
    ray.color(rainbow_color)
    # Create the five pointed stars
    for side in range(5):
        ray.forward(50)
        ray.right(144)
    # Move for the next position to start the next star
    ray.penup()
    ray.left(60)
    ray.forward(60)
    ray.pendown()

# Move away from the stars without drawing to start the rainbow
ray.penup()
ray.right(90)
ray.forward(100)
ray.right(90)
ray.forward(50)
ray.right(180)
ray.pendown()

# Draw a line in each color, moving to the next line each time, going back in the initial horizontal position
for rainbow_color in rainbow:
    ray.color(rainbow_color)
    ray.forward(100)
    ray.penup()
    ray.right(90)
    ray.forward(5)
    ray.right(90)
    ray.forward(100)
    ray.right(180)
    ray.pendown()
