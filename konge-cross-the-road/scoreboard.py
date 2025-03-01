FONT = ("Courier", 24, "normal")
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}",align="center",font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align="center", font=FONT)
