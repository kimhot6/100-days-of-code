from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'bold')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(270)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.print_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.print_score()
