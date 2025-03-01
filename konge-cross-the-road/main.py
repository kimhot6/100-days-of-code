from turtle import Turtle, Screen
from time import sleep
from random import random
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.title("Konge Crosses the Road!")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(player.move_forward,"Up")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    if random() > 0.8:
        car_manager.generate_car()

    #Reached the Goal
    if player.ycor() > 280:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.update_level()

    #Detect Collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 30 and abs(player.ycor()-car.ycor()) < 18:
            game_is_on = False
            scoreboard.game_over()

    car_manager.move_cars()

screen.exitonclick()
