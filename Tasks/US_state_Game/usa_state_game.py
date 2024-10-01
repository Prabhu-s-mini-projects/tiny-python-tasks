""" Game to identify the state of USA"""
# Dependencies
import turtle as controller
import pandas

# CONSTANTS
STATES_CSV_PATH = "Database/50_states.csv"
BLANK_STATE_IMAGE = "Database/blank_states_img.gif"
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')

def main()-> None:
    """ start of a program"""
    # Creating a game window
    game_window = controller.Screen()
    game_window.title("U.S STATE GAME")

    # adding an image as a new shape in the screen
    game_window.addshape(BLANK_STATE_IMAGE)

    # updating the screen with image
    controller.shape(BLANK_STATE_IMAGE) # pylint: disable=no-member

    # Display the input pop-up box
    answer = game_window.textinput(title="Guess the State GAME",
                                   prompt ="Whats the another state name?").title()

    # Fetching the states
    usa_states = pandas.read_csv(STATES_CSV_PATH)
    all_states = usa_states.state.to_list()
    guessed_states = []

    def update_state_name(state_details)-> None:
        """ Updates the state name in the image"""

        name_board = controller.Turtle()
        name_board.penup()

        # Moves the name of the state to X Y position on the screen
        name_board.goto(state_details.x.item(),state_details.y.item())

        name_board.write(f"{state_details.state.item()}", align=ALIGNMENT, font=FONT)

        name_board.hideturtle()

    score = 0
    while score < 50:
        if answer == "Exit":
            # Calculating the missing states
            missing_states = [state.upper() for state in all_states if state not in guessed_states]

            # writes the missing state data to csv file
            new_data  = pandas.DataFrame(missing_states)
            new_data.to_csv("Missing_States.csv")
            break
        if answer in all_states and answer not in guessed_states:
            score += 1
            # Fetching a row based on the state name
            state = usa_states[usa_states["state"] == answer]

            # Updating it in the map
            update_state_name(state)

            # Added in to guessed state list
            guessed_states.append(state.state.item())

        answer = game_window.textinput(title=f"{score}/50 state",
                                       prompt="Whats the another state name?").title()

    game_window.mainloop()

if __name__ == '__main__':
    main()

# # Below code is take the X and Y parameter from the screen and stored in CSV file.
# def get_mouse_click(x:float,y:float)-> None:
#     print(x,y)
#
# game_window.onscreenclick(get_mouse_click)
