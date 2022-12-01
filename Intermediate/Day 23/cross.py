import time
from turtle import Screen
from player import Player
from cars import CarManager
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
score_board = ScoreBoard()
screen.onkey(key="Up", fun=player.move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.is_at_finish():
        player.go_to()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()