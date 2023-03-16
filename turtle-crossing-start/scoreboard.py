from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 240)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over.", align="center", font=FONT)