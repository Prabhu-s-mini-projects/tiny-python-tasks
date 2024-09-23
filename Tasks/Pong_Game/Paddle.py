import turtle as controller

# CONSTANTS
LEFT_PADDLE_X_COORDINATE = -280
RIGHT_PADDLE_X_COORDINATE = 270
MAX_TOP_COORDINATE = 280
MAX_BOTTOM_COORDINATE =-280



class Paddle(controller.Turtle):

    def __init__(self,side:str):
        super().__init__("square")
        self.side = side
        self.penup()
        self.color("white")
        self.create_paddle(self.side)
        self.x_move = 5
        self.y_move = 10


    def create_paddle(self,side:str) -> None:
        """
        Create paddle and place it correct position based on the side
        """
        if side == "ball":
            self.shape("circle")
            self.shapesize(stretch_wid=1,stretch_len=1)
        elif side == "wall":
            self.shapesize(stretch_wid=100, stretch_len=0.05)
            self.goto(0,0)
        else:
            self.shapesize(stretch_wid=5,stretch_len=1)
            self.goto(LEFT_PADDLE_X_COORDINATE if side =="left" else RIGHT_PADDLE_X_COORDINATE ,0 )

    def up(self) -> None:
        """Moves the paddle up """
        if self.ycor() < MAX_TOP_COORDINATE:
            self.goto(self.xcor(),self.ycor()+20)

    def down(self) -> None:
        """Moves the paddle down"""
        if self.ycor() > MAX_BOTTOM_COORDINATE:
            self.goto(self.xcor(),self.ycor() -20)

    def move(self) -> None:
        """Moves the ball"""
        self.goto(self.xcor() + self.x_move,self.ycor() + self.y_move)

    def bounce(self) -> None:
        """ bounce back from wall"""
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *= -1