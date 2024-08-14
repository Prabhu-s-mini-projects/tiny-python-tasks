import Coffee_machine_Utils_methods as Machine

Machine.load_logo()

# # Todo:1
# 1. Get user input in a loop with a condition machine state on.
machine_ON = True
while machine_ON:
    user_ask = input("What would you like? (espresso/latte/cappuccino:)\t")
    if Machine.is_valid(user_ask):
        # 2. Based on the userinput call the respective methods once the action is completed return it back to the loop.
        machine_ON = Machine.perform_task(user_ask)
    else:
        print(f"Please enter the Valid input: {user_ask} is not valid ask")
