COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.hideturtle()
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_cars=random.randint(1,6)
        if random_cars==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed+=MOVE_INCREMENT
            