""" Contains ScoreBoard class"""

import  turtle as controller


# CONSTANTS
from snake import DEFAULT_LENGTH
ALIGNMENT ="center"
FONT = ('Courier', 24, 'normal')
TITLE_POSITION = (0,270)
NUMBER_OF_LIVES = 3
LIVES_POSITION = (-220,220)

class ScoreBoard(controller.Turtle):
    """
    Scoreboard is a Turtle
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.high_score = self.get_highscore()
        self.lives = ["*","*","*"]
        self.refresh(DEFAULT_LENGTH)
        self.report_lives()

    def refresh(self,snake_length: int) -> None:
        """refresh the scorecard"""
        self.clear()
        self.goto(TITLE_POSITION)
        self.write(f"Score : {snake_length-DEFAULT_LENGTH}"
                   f" High Score : {self.high_score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
        self.report_lives()

    def reset_game(self, snake_length: int)-> None:
        """resets the game"""
        if self.high_score < (snake_length-DEFAULT_LENGTH):
            self.high_score = snake_length-DEFAULT_LENGTH
            self.set_highscore()
        self.refresh(DEFAULT_LENGTH)
        self.lives.pop()
        #self.report_lives() Will be fixed later

    def report_game_over(self) -> None:
        """ game over"""
        self.home()
        self.color("red")
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def report_lives(self)-> None:
        """reports lives"""
        self.goto(LIVES_POSITION)
        self.color("red")
        self.write(f"{self.lives}", align=ALIGNMENT, font=FONT)

    def get_highscore(self)-> int:
        """gets the high score"""
        with open("database.txt", encoding="utf-8") as database:
            highscore =  int(database.read())
        return highscore

    def set_highscore(self)-> None:
        """set the high score"""
        with open("database.txt","w", encoding="utf-8") as database:
            database.write(f"{self.high_score}")
