FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0, 280)
        self.write("Scoreboard",False, align="center", ("Arial", 24, "normal"))
