"""Contains scoreboard class"""
# Dependencies
from turtle import Turtle


# CONSTANTS
ALIGNMENT ="center"
FONT = ('Courier', 24, 'normal')
POSITION = (-230,250)


class Scoreboard(Turtle):
    """
    Creates an instance to maintain the score
    """

    def __init__(self, side='0'):
        super().__init__(side)
        self.penup()
        self.color("white")
        self.level = 0
        self.refresh(self.level)

    def refresh(self,score:int) -> None:
        """refresh the score count"""
        self.clear()
        self.goto(POSITION)
        self.write(f"Level: {score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_level(self) -> None:
        """Increases the score by 1"""
        self.level += 1
        self.refresh(self.level)

    def report_game_over(self) -> None:
        """Displays the game over a message"""
        self.home()
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
