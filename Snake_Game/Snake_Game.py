import  turtle as controller
from itertools import count
from Snake import Snake
import time


# Setting up the GAME place
window = controller.Screen()
window.setup(height=600, width=600)
window.bgcolor("black")
window.title("Snake_Game")
window.tracer(0)

# Creating a snake Body
snake = Snake()

window.update()




# Moving the snake
game_over = False
# count = 0
while not game_over:
    window.update() # To update the screen all the segments
    snake.move()
    time.sleep(0.1)


window.exitonclick()