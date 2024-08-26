# Required packages
import turtle as controller

# Constants
DEFAULT_LENGTH = 3
MOVE_DISTANCE = 20
DIRECTIONS ={
    "RIGHT" : 0,
    "UP"    : 90,
    "LEFT"  : 180,
    "DOWN"  : 270
}


class Snake:

    def __init__(self):
        """
        attributes of Snake
        """
        self.snake_body:list = []
        self._create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[len(self.snake_body)-1]

    def _create_snake(self) -> None:
        """
        Constructs the Snake based on the attributes
        """
        for seg_position in range(1, DEFAULT_LENGTH + 1):
            snake_seg = controller.Turtle("square")
            snake_seg.penup()
            snake_seg.color("white")
            snake_seg.goto(20 * seg_position, 0)
            self.snake_body.append(snake_seg)

    def grow(self) -> None:
        """
        grows by 1 segment
        """
        snake_seg = controller.Turtle("square")
        snake_seg.penup()
        snake_seg.color("white")
        position = self.tail.position()
        snake_seg.goto(position)
        self.snake_body.append(snake_seg)


    def move(self)-> None:
        """
        Moves the Snake
        """
        length = len(self.snake_body) - 1
        while length > 0:
            next_pos = self.snake_body[length - 1].position()
            self.snake_body[length].goto(next_pos)
            length -= 1
        self.head.forward(MOVE_DISTANCE)

    def up(self)-> None:
        """
        changes Heading direction to up
        """
        if self.head.heading() != DIRECTIONS["DOWN"]:
            self.head.setheading(DIRECTIONS.get("UP"))

    def down(self) -> None:
        """
        changes Heading direction to down
        """
        if self.head.heading() != DIRECTIONS["UP"]:
            self.head.setheading(DIRECTIONS.get("DOWN"))

    def left(self) -> None:
        """
        changes Heading direction to LEFT
        """
        if self.head.heading() != DIRECTIONS["RIGHT"]:
            self.head.setheading(DIRECTIONS.get("LEFT"))

    def right(self) -> None:
        """
        changes Heading direction to RIGHT
        """
        if self.head.heading() != DIRECTIONS["LEFT"]:
            self.head.setheading(DIRECTIONS.get("RIGHT"))
