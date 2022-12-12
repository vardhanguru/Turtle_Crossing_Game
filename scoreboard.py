from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-50,320)
        self.score=0
        self.write(f"score is {self.score}",font=FONT)
    def update(self):
        self.clear()
        self.write(f"score is {self.score}",font=FONT)



