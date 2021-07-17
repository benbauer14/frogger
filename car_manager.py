COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle, setheading
import random

cars = []
lanes = [-240, -180, - 120, -60, 0, 60, 120, 180, 240 ]

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

    def createCar():
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=3)
        new_car.lane(lanes(random.randint(0,8))
        if(new_car.lane() % 120 = 0 ):
            new_car.setheading(180)
        else:
            new_car.setheading(0)