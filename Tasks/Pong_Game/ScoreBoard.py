import turtle as controller

ALIGNMENT ="center"
FONT = ('Courier', 60, 'normal')
LEFT_SCORE_POSITION = (40,240)
RIGHT_SCORE_POSITION = (-40,240)

class Scoreboard(controller.Turtle):
    """

    """
    def __init__(self,side:str):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.side = side
        self.refresh(self.score)

    def refresh(self,score:int) -> None:
        self.clear()
        self.goto(LEFT_SCORE_POSITION if self.side == "left" else RIGHT_SCORE_POSITION)
        self.write(f"{score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_count(self) -> None:
        self.score += 1
        self.refresh(self.score)
