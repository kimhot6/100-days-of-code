START_SPEED = 10
DELAY = 0.1

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.delay = DELAY
        self.x_speed = START_SPEED
        self.y_speed = START_SPEED

    def move(self):
        x_cor = self.xcor() + self.x_speed
        y_cor = self.ycor() + self.y_speed
        self.goto((x_cor,y_cor))

    def bounce_x(self):
        self.x_speed *= -1
        self.delay *= 0.9

    def reset_position(self):
        self.home()
        self.x_speed *= -1
        self.delay = DELAY
