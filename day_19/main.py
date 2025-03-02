from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ["thistle", "lavender", "rosybrown", "seagreen", "springgreen"]
guess = screen.textinput("GoGo", "Which konge do you love")

konge = []
for i in range(5):
    konge.append(Turtle(shape="turtle"))
    konge[i].color(colors[i])
    konge[i].up()
    konge[i].goto(-230, 60 - 30*i)



screen.exitonclick()
