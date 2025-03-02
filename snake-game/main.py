from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("rosybrown")
screen.title("Let's go konge!")
screen.tracer(0)
konge = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(konge.left,"Left")
screen.onkey(konge.right,"Right")
screen.onkey(konge.up, "Up")
screen.onkey(konge.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    konge.move()

    #Detect collision with food
    if konge.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        konge.extend()

    #Detect collision with wall
    if abs(konge.head.xcor()) > 285 or abs(konge.head.ycor()) > 285:
        scoreboard.reset()
        konge.reset()

    #Detect collision with tail.
    for segment in konge.segments[1:]:
        if konge.head.distance(segment) < 1:
            scoreboard.reset()
            konge.reset()

screen.exitonclick()
