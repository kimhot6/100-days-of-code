from turtle import Turtle

class CorrectState(Turtle):
    def __init__(self, state_name, coor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(coor)
        self.write(arg=state_name,align="center",font={"Arial",20,"Bold"})
