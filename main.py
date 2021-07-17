import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

frog = Player()
scoreboard = Scoreboard()
cars = []
lanes = [-240, -180, - 120, -60, 0, 60, 120, 180, 240 ]
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(frog.moveForward, "Up")
screen.onkey(frog.moveLeft, "Left")
screen.onkey(frog.moveRight, "Right")
frog.goto(0, -275)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()