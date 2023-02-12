from turtle import Turtle
FONT = 24
ALIGNMENT = "left"


class LevelBoard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.goto(-260, 250)
        self.hideturtle()
        self.write(f"Level: {self.level}", True, align=ALIGNMENT, font=("Ariel", FONT, "normal"))

    def increase_level(self):
        self.clear()
        self.goto(-260, 250)
        self.level += 1
        self.write(f"Level: {self.level}", True, align=ALIGNMENT, font=("Ariel", FONT, "normal"))


