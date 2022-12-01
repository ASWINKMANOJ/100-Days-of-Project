FONT = ("Courier", 24, 'normal')

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-280, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

    def increase_level(self):
        self.level += 1
        self.update_score()
