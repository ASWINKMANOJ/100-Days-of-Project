from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG!")
screen.tracer(0)
r_position = (350, 0)
l_position = (-350, 0)
l_p = Paddle(l_position)
r_p = Paddle(r_position)
ball = Ball()
score = ScoreBoard()
is_game_on = True

screen.listen()
screen.onkey(key="Up", fun=r_p.up)
screen.onkey(key="Down", fun=r_p.down)
screen.onkey(key="w", fun=l_p.up)
screen.onkey(key="s", fun=l_p.down)

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision paddle
    if (ball.distance(r_p) < 50 and ball.xcor() > 320) or (ball.distance(l_p) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()
