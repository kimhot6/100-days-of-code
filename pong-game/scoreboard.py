from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.pencolor("white")
        self.l_score = 0
        self.r_score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.print_score()

    def r_point(self):
        self.r_score += 1
        self.print_score()
