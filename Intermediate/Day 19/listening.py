from turtle import Turtle, Screen
import random
import turtle as s

t = Turtle()
screen = Screen()
s.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)


def move_forward():
    t.forward(30)


def move_back():
    t.back(30)


def turn_right():
    new_heading = t.heading() + 10
    t.setheading(new_heading)


def turn_left():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def increase():
    current = t.pensize() + 5
    t.pensize(current)


def decrease():
    pensize = t.pensize()
    if pensize > 5:
        current = t.pensize() - 5
        t.pensize(current)


def default():
    t.color(0, 0, 0)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def up():
    t.penup()


def down():
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="r", fun=random_color)
screen.onkey(key="h", fun=increase)
screen.onkey(key="l", fun=decrease)
screen.onkey(key="space", fun=default)
screen.onkey(key="c", fun=clear)
screen.onkey(key="u", fun=up)
screen.onkey(key="y", fun=down)

screen.exitonclick()
