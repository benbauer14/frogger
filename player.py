STARTING_POSITION = (0, -275)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle, ycor

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()

    def moveLeft(self):
        if(self.xcor() > -275):
            self.goto(self.xcor() - 20, self.ycor())

    def moveRight(self):
        if(self.xcor() < 255):
            self.goto(self.xcor() + 20, self.ycor())
    
    def moveForward(self):
        self.goto(self.xcor(), self.ycor() + 20)