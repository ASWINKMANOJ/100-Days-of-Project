import turtle as s
from turtle import Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


t = s.Turtle()
s.colormode(255)

t.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + gap_size)


draw_spirograph(3)

screen = Screen()
screen.exitonclick()
