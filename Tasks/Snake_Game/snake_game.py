"""Main Scirpt of the game"""
import time
import  turtle as controller

from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def main()-> None:
    """Start of program"""

    # Setting up the GAME place
    window = controller.Screen()
    window.setup(height=600, width=600)
    window.bgcolor("black")
    window.title("Snake_Game")
    window.tracer(0)

    # Creating a snake Body
    snake = Snake()
    food = Food()
    scoreboard =  ScoreBoard()
    window.update() # update the window to display snake

    window.listen()
    # mapping the key and methods
    window.onkey(snake.up,"Up")
    window.onkey(snake.down,"Down")
    window.onkey(snake.left,"Left")
    window.onkey(snake.right,"Right")

    game_over = False

    def game_over_sequence()->None:
        """execute the game over sequences"""

        if scoreboard.lives:
            snake.head.home()
            scoreboard.reset_game(len(snake.snake_body))
            for seg in snake.snake_body[3:]:
                snake.snake_body.remove(seg)
        else:
            #global game_over
            game_over = True
            scoreboard.report_game_over()

    while not game_over:
        window.update() # To update the screen after the segments complete taking first step
        snake.move()
        time.sleep(0.1)
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow()
            scoreboard.refresh(len(snake.snake_body))

        # Detect the collusion.
        if not -290 < snake.head.xcor() < 290 or  not -290 < snake.head.ycor() < 290:
            game_over_sequence()

        # Detecting the tail.
        for segment in snake.snake_body:
            if segment.position() == snake.head.position():
                pass
            elif snake.head.distance(segment) < 10:
                game_over_sequence()

    window.exitonclick()

if __name__ == '__main__':
    main()