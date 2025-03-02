MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.add_segment((-20*i,0))
        self.head = self.segments[0]

    def add_segment(self, position):
        square = Turtle("square")
        square.color("aliceblue")
        square.speed("fastest")
        square.up()
        square.goto(position)
        self.segments.append(square)

    def extend(self):
        tail_position = self.segments[-1].position()
        self.add_segment(tail_position)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        for i in range(3):
            self.add_segment((-20*i,0))
        self.head = self.segments[0]
