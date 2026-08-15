import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = CarManager()
user = Player()
scoreboard = Scoreboard()
sleep_value  = .1

screen.listen()
screen.onkeypress(user.up, key= "Up")
screen.onkeypress(user.down, key= "Down")

game_is_on = True
while game_is_on:
    thingy = [cars.create_cars()]
    cars.move()
    time.sleep(sleep_value)
    screen.update()

    #Detect Collision
    for car in cars.all_cars:
        if user.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Completing a level
    if user.ycor() == 280:
        user.next_level()
        sleep_value *=.7
        scoreboard.increase_level()


screen.exitonclick()




