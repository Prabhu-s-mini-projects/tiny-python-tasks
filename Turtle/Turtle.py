import turtle
from turtle import  *
import heroes
import villains
import random



t_jack = Turtle()
t_jack.shape("turtle")

# Faster animation
t_jack.speed("fastest")
turtle.colormode(255)

def random_color() -> tuple:
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

radius = 150
n = 1
for angle in range(360):
    t_jack.pencolor(random_color())
    t_jack.circle(radius)
    t_jack.left(2)

# t_jack.color("red")
#
# for _ in range(0,15):
#     t_jack.forward(10)
#     t_jack.penup()
#     t_jack.forward(10)
#     t_jack.pendown()
#
# t_jack.color("green")
# for _ in range(0,4):
#     t_jack.forward(10)
#     t_jack.left(90)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# Draw differt shape
for shape in range(3,11):
    # get a random color
    t_jack.pencolor(random_color())
    for _ in range(0,shape):
        t_jack.forward(100)
        t_jack.left(360/shape)


# changes the width and color of a line
t_jack.pensize(10)


# Random turns
directions = [0, 90, 180, 270]
for _ in range(100):
    t_jack.forward(15)
    t_jack.pencolor(random_color())
    t_jack.setheading(random.choice(directions))


t_jack.pensize(1)


print(t_jack)

# Game Area
window  = Screen()
window.delay(100)
print(window.canvheight)
window.exitonclick()

print(window.delay())

print(window.delay())
print(heroes.gen())
print(villains.gen())



from prettytable import PrettyTable

table  = PrettyTable()

#
# table.field_names = ["PokeMon Name", "Type"]
# table.add_rows(["Pikachu", "Electric"])
# table.add_rows(["Squirtle", "Water"])
# table.add_rows(["Charmander", "Fire"])

# table.add_column("PokeMon",["pikachu", "squritle", "Charmander"])
# table.add_column("type",["electric", "water", "Fire"])
# table.align = 'l'



print(table)
