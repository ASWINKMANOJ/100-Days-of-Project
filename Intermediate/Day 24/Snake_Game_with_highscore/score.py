from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        with open("high_scores.txt") as score:
            self.high_score = int(score.read())
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE:{self.score}  HighScore:{self.high_score} ", align="center", font=("Arial", 14, "normal"))

    def increase(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align="center", font=("Arial", 14, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_scores.txt", mode="w") as scores:
                scores.write(f"{self.high_score}")

        self.score = 0
        self.update_score()