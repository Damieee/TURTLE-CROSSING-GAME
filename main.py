import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard=Scoreboard()
car_manager=CarManager()
screen = Screen()
screen.tracer(0)
player=Player()
screen.setup(width=600, height=600)
screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()

    if player.reach_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_score()
    
screen.exitonclick()