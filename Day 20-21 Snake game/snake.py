from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(0, 3):
            new_seg = Turtle("square")
            new_seg.color('white')
            new_seg.penup()
            self.segments.append(new_seg)

        x = 0
        for segment in self.segments:
            segment.goto(x, 0)
            x -= 20

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.segments[0].fd(20)