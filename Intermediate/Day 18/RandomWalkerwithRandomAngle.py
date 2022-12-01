import turtle as s
from turtle import Screen
import random

t = s.Turtle()
s.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_color = (r, g, b)
    return ran_color


t.pensize(2)
t.speed("fast")

n = 1000
s = 0
options = [0, 90, 180, 270]
while n > s:
    t.hideturtle()

    s += 1
    t.penup()
    t.dot(30, random_color())
    t.forward(20)
    t.setheading(random.choice(options))

screen = Screen()
screen.exitonclick()
