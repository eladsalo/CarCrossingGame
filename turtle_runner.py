from turtle import Turtle


class TurtleRunner(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -290)

    def up(self):
        self.forward(20)