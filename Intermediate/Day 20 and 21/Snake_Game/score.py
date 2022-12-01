from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(f"SCORE:{self.score}", align="center", font=("Arial", 14, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Arial", 14, "normal"))
