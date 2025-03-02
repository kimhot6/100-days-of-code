import random
import turtle
import colorgram

# colors = colorgram.extract('mountain.jpg', 30)
# for colour in colors:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     palette.append((r, g, b))
#
# print(palette)


palette = [(97, 162, 221), (60, 102, 159), (19, 28, 45), (59, 129, 208), (195, 221, 239), (38, 31, 24), (103, 92, 82), (170, 155, 141), (240, 236, 228), (35, 29, 33), (41, 61, 96), (239, 243, 242), (94, 87, 90), (160, 193, 227), (27, 31, 27), (156, 149, 153), (88, 93, 89), (159, 164, 161), (72, 67, 46), (135, 205, 245), (238, 235, 237), (143, 130, 105), (210, 193, 165), (73, 59, 56), (68, 60, 64), (140, 123, 117), (133, 124, 128), (207, 186, 178), (60, 66, 59), (187, 194, 190)]

turtle.shape("turtle")
turtle.speed("fastest")
turtle.color("thistle")
turtle.colormode(255)
turtle.hideturtle()

def color_line():
    for _ in range(10):
        turtle.dot(20, random.choice(palette))
        turtle.forward(50)

turtle.up()
for row in range(10):
    turtle.goto(-250,-200 + row * 50)
    color_line()

screen = turtle.Screen()
screen.exitonclick()
