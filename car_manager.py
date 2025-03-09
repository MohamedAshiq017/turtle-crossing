from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__
        self.carlist=[]

    def create_cars(self):
        car=Turtle("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2,stretch_wid=1)
        car.penup()
        y_pos=(random.randint(-24,24))*10
        car.goto(300,y_pos)
        self.carlist.append(car)


    def run_cars(self,level):
        for car in self.carlist:
            car.setheading(180)
            if level > 0:
                car.forward(level*MOVE_INCREMENT)
            else:
                car.forward(STARTING_MOVE_DISTANCE)







