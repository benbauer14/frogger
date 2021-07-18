import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

frog = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(frog.moveForward, "Up")
screen.onkey(frog.moveLeft, "Left")
screen.onkey(frog.moveRight, "Right")
frog.goto(0, -265)

game_is_on = True
delay = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.createCar()
    cars.move()
    for car in cars.cars:
        if(frog.distance(car) < 10):
            game_is_on = False
            scoreboard.clear()
            scoreboard.write("SMASH!", move=False, align="center", font=("Arial", 20, "normal"))
    if(frog.ycor() > 250):
            scoreboard.write("WINNER!", move=False, align="center", font=("Arial", 20, "normal"))

screen.exitonclick()