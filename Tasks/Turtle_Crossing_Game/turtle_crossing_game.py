""" main scrpit of program"""
# Dependencies
import time
import turtle as controller

# Internal Modules
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard


def main()-> None:
    """Start of a program"""
    # Creating a Gaming Window
    game_window = controller.Screen()
    game_window.setup(width=600,height=600)
    game_window.bgcolor("black")
    game_window.title("Turtle Crossing Game")
    game_window.tracer(0)

    # Create the objects of the games
    scoreboard = Scoreboard()
    player_turtle = Player()
    car_manager = CarManager()

    # Mapping the key to the turtle Movement
    game_window.listen()
    game_window.onkey(player_turtle.move,"Up")
    game_window.update()

    # Keep the game running
    game_over= False
    #count = 0
    number_of_car = 10
    while not game_over:
        game_window.update()
        car_manager.create_car()
        time.sleep(0.1)
        car_manager.move_cars(scoreboard.level)

        # After reaching the finish line. Increment the level and move it start position
        if player_turtle.ycor() > 250:
            player_turtle.go_to_start()
            scoreboard.increase_level()
            number_of_car -= 1

        # Detect the collusion
        for car in car_manager.cars_in_lanes:
            if car.distance(player_turtle) < 20:
                scoreboard.report_game_over()
                game_over = True

    game_window.exitonclick()

if __name__ =='__main__':
    main()
