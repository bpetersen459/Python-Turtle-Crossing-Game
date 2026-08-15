from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-287, 255)
        self.write(arg= f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", align="center", font=FONT)
