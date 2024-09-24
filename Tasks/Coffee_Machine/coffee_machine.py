""" Main application file"""

import coffee_machine_utils_methods as machine

def main()-> None:
    """
    main loop keeps the program running
    :return:
    """
    # Loads the logo of the game
    machine.load_logo()

    # 1. Get user input in a loop with a condition machine state on.
    machine_on = True
    while machine_on:
        user_ask = input("What would you like? (espresso/latte/cappuccino:)\t")
        if machine.is_valid(user_ask):
            # 2. Based on the userinput call the respective methods
            # once the action is completed, return it to the loop.
            machine_on = machine.perform_task(user_ask)
        else:
            print(f"Please enter the Valid input: {user_ask} is not valid ask")

if __name__ == "__main__":
    main()
