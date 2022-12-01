from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
# Listen to the input given through the keyboard and make the snake move accordingly
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.update()
game_is_on = True

# Make the snake move continuously until the game_is_on gets False
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food and extend the snake by square.
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase()
        snake.extend()

    # Detect collision with the wall.
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 290:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
