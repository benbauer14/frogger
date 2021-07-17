COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5)

    def move(self, speed, direction):
        if(direction == "left"):
            self.setheading(180)
        elif(direction == "right"):
            self.setheading(0)
