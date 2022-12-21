from turtle import Turtle

class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.pensize(3)
        self.create_net()

    def create_net(self):
        self.penup()
        self.setheading(270)
        self.backward(300)
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)