"""Main script of program"""
import  turtle
import random

def main()->None:
    """Start a game"""

    #Preparing racetrack.
    race_track = turtle.Screen()
    race_track.setup(height=500,width=540)

    #ask Player  to bet
    player_bet = race_track.textinput(title="Please place your bet", prompt="Which turtle will win the race? \n"
                                                                            " Enter a color:\t")
    print(player_bet)

    colors = ["red", "blue", "green","purple", "black","orange","violet"]
    y_position = [-100,-70, -40, -10, 20, 50, 80]
    race_turtles = []
    # creating Turtles
    for color in colors:
        color_turtle = turtle.Turtle(shape="turtle")
        color_turtle.penup()
        color_turtle.color(color)
        color_turtle.goto(-250,y_position[colors.index(color)])
        race_turtles.append(color_turtle)


    is_race_on =True

    while is_race_on:
        for race_turtle in race_turtles:
            if race_turtle.xcor() > 230:
                is_race_on = False
                if player_bet == race_turtle.pencolor():
                    print("you won")
                else:
                    print("you lose")
            race_turtle.forward(random.randint(1,10))





    race_track.exitonclick()

if __name__ == '__main__':
    main()

