"""Contains food class"""
import random
import turtle as controller


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

    def return_shape(self) -> None:
        """ created a dummy method"""
        print(random.randint(0, 5))
        print(random.randint(5, 9))

    def refresh(self)-> None:
        """Goes to new location"""
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)
