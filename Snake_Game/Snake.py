import  turtle as controller

class Snake:

    def __init__(self):
        """
        Constructing the Snake with default size as 3 seg
        """
        self.snake_length = 3
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for seg_position in range(1, self.snake_length + 1):
            snake_seg = controller.Turtle("square")
            snake_seg.penup()
            snake_seg.color("white")
            snake_seg.goto(20 * seg_position, 0)
            self.snake_body.append(snake_seg)

    def move(self):
            # moving the body
            length = len(self.snake_body) - 1
            while length > 0:
                next_pos = self.snake_body[length - 1].position()
                self.snake_body[length].goto(next_pos)
                length -= 1
            self.snake_body[0].forward(20)