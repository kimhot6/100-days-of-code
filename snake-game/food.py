from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.up()
        self.shapesize(0.5, 0.5)
        self.color("thistle")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)