from turtle import Turtle
import random

COLOURS = ["red", "yellow", "blue", "purple", "green", "orange"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLOURS))
        self.goto(280, (random.randint(-280, 280)/40)*40)


