COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle, color, setheading
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.lanes = [-240, -180, - 120, -60, 0, 60, 120, 180, 240 ]

    def move(self):
        for car in range(0,len(self.cars) - 1):
            self.cars[car].forward(30)

    def createCar(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.color(COLORS[random.randint(0,5)])
        new_car.lane = self.lanes[random.randint(0,8)]
        if(new_car.lane % 120 == 0 ):
            new_car.setheading(180)
            new_car.goto(300, new_car.lane)
        else:
            new_car.setheading(0)
            new_car.goto(-300, new_car.lane)
        new_car.velocity = random.randint(10,30)
        self.cars.append(new_car)
        
