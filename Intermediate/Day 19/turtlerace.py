from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which tutle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'purple', 'blue', 'green']
y = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y[turtle_index])
    all_turtle.append(new_turtle)


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = (turtle.pencolor())
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
                break
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
                break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
