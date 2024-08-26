import  turtle as controller
import random

class Food(controller.Turtle):
    """
    inherits the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()

    def refresh(self)-> None:
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)
