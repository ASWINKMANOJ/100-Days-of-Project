from turtle import Turtle, Screen
import random

t = Turtle()

t.shape("turtle")
t.color("cyan")
color = ["violet", "indigo", "blue", "green", "yellow", "orange", "red", "cyan", "grey"]
t.pensize(3)
random.shuffle(color)
print(color)
r = 0


for i in range(3, 18):
    if r >= len(color):
        r = r % len(color)
        random.shuffle(color)
    t.color(color[r])
    r += 1
    for j in range(i):
        t.forward(30)
        a = ((i - 2) * 180) / i
        a = 180 - a
        t.left(a)
        t.forward(30)

screen = Screen()
screen.exitonclick()
