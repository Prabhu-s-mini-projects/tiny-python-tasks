"""Contains Car manager class"""
# Dependencies
import random
from turtle import Turtle as Car

# Internal Modules
# N/A

# CONSTANTS
COLORS = ["red","blue","yellow","green","orange","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_NUM_OF_CARS_START = 3

class CarManager:
    """
    Roles: TBD
    """
    def __init__(self):
        self.cars_in_lanes = []
        self.create_car()

    def create_car(self)->None:
        """Creates a car and place it start position"""
        if random.randint(1,6) == 1:
            car  = Car("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, random.randint(-25, 20) * 10)
            car.setheading(180)
            self.cars_in_lanes.append(car)


    def move_cars(self,level: int)->None:
        """
        Move the cars in the lanes
        """
        car_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level
        for car in self.cars_in_lanes:
            car.forward(car_speed)
