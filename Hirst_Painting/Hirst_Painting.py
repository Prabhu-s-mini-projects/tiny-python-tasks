from turtle import Turtle, Screen

import colorgram
import random
import turtle

from PIL.Image import radial_gradient


def extract_color()-> list:
    # Extract 6 colors from an image.
    colors = colorgram.extract('image.jpg', 60)
    rgb_color = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_color.append((r,g,b))

    return rgb_color

# Extract color and give you color list
color_container = extract_color()

# Creating a turtle
timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.speed("fastest")
turtle.colormode(255)

timmy_turtle.penup()
timmy_turtle.hideturtle()

timmy_turtle.setheading(225)
timmy_turtle.forward(300)
timmy_turtle.setheading(0)

start_place = timmy_turtle.position
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy_turtle.dot(20, random.choice(color_container))
    timmy_turtle.fd(50)
    if dot_count % 10 == 0:
        timmy_turtle.setheading(90)
        timmy_turtle.forward(50)
        timmy_turtle.setheading(180)
        timmy_turtle.forward(500)
        timmy_turtle.setheading(0)

canvas = Screen()
canvas.exitonclick()