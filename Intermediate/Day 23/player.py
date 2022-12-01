STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.go_to()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def go_to(self):
        self.goto(STARTING_POSITION)