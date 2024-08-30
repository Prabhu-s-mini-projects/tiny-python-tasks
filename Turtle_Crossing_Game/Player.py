# Dependencies
from turtle import Turtle


# Internal modules

# CONSTANTS
STARTING_POSITION = (0,-280)
FINISH_LINE = 260
MOVE_DISTANCE = 10

class Player(Turtle):
    """
    Player to cross the road.
    """
    def __init__(self):
        super().__init__("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self)->None:
        """Makes Player to take a step"""
        if self.ycor() < FINISH_LINE:
            self.forward(MOVE_DISTANCE)

    def go_to_start(self)->None:
        """
        """
        self.goto(STARTING_POSITION)
