FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.speed(0)
        self.write("", move=False, align="center", font=("Arial", 20, "normal"))
