Speed = 20

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.up()
        self.goto(position)

    def go_up(self):
        self.sety(self.ycor() + Speed)

    def go_down(self):
        self.sety(self.ycor() - Speed)
