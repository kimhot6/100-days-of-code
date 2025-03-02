# from turtle import Turtle, Screen
#
# konge = Turtle()
# screen = Screen()
#
# konge.color("CornflowerBlue", "AliceBlue")
# konge.shape("turtle")
# konge.forward(100)
# screen.exitonclick()
# print(screen.canvheight)
#
#

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table.align)
print(table)
