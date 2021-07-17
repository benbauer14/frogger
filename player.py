STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle, ycor

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")

    def moveLeft(self):
        self.goto(self.xcor() + 20)

    def moveRight(self):
        self.goto(self.xcor() - 20)
    
    def moveForward(self):
        self.goto(self.ycor() + 20)