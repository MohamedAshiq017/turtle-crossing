import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turt=Player()

cm=CarManager()
score=Scoreboard()
screen.onkeypress(key="Up",fun=turt.Move_up)


game_is_on = True
seconds=0
while game_is_on:
    seconds+=1
    time.sleep(0.1)
    if seconds % 6 ==0:
        cm.create_cars()
    cm.run_cars(score.level)
    screen.update()

    for car in cm.carlist:
        if turt.distance(car)<23:
            game_is_on=False
            score.game_over()

    if turt.ycor()>=300:
        score.update_score()
        turt.goto(0,-280)

screen.exitonclick()

