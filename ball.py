from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.setheading(45)
        self.move()

    def move(self):
        self.speed('slow')
        self.forward(20)
