import turtle
from tkinter import mainloop
from turtle import Turtle, Screen
import random

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    return (R,G,B)

konge = Turtle()
konge.shape("turtle")
konge.color("cornflowerblue", "aliceblue")
konge.speed("fastest")


while True:
    konge.pencolor(change_color())
    konge.circle(100)
    konge.left(10)




# while True:
#     konge.pencolor(change_color())
#     konge.setheading(random.randrange(0,360,90))
#     konge.forward(30)


screen = Screen()
screen.exitonclick()
