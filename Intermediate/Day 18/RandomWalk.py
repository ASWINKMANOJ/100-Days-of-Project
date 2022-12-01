import turtle as s
from turtle import Screen
import random

t = s.Turtle()
s.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
t.pensize(10)
t.speed("fast")
options = [0, 90, 180, 270]

n = int(input("any number"))
s = 0

while n > s:
    s += 1
    t.color(random_color())
    t.forward(20)
    t.setheading(random.choice(options))

screen = Screen()
screen.exitonclick()

