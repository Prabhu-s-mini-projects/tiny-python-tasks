import  turtle as controller
from Snake import DEFAULT_LENGTH
ALIGNMENT ="center"
FONT = ('Courier', 24, 'normal')
TITLE_POSITION = (0,270)

class ScoreBoard(controller.Turtle):
    """
    Scoreboard is a Turtle
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.refresh(DEFAULT_LENGTH)

    def refresh(self,snake_length: int) -> None:
        self.clear()
        self.goto(TITLE_POSITION)
        self.write(f"Score : {snake_length-DEFAULT_LENGTH}",align=ALIGNMENT,font=FONT)
        self.hideturtle()

    def report_game_over(self) -> None:
        self.home()
        self.color("red")
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)