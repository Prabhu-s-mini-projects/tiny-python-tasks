""" Main application file"""

import coffee_machine_utils_methods as Machine

def main()-> None:
    """
    main loop keeps the program running
    :return:
    """
    # Loads the logo of the game
    Machine.load_logo()

    # 1. Get user input in a loop with a condition machine state on.
    machine_on = True
    while machine_on:
        user_ask = input("What would you like? (espresso/latte/cappuccino:)\t")
        if Machine.is_valid(user_ask):
            # 2. Based on the userinput call the respective methods
            # once the action is completed return it back to the loop.
            machine_on = Machine.perform_task(user_ask)
        else:
            print(f"Please enter the Valid input: {user_ask} is not valid ask")

if __name__ == "__main__":
    main()
