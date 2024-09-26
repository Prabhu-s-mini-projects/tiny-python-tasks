"""Main script Simple calculator"""
import database as Db

def main()-> None:
    """start of a program"""
    # Loading the calculator
    print(Db.LOGO)

    # Get user input:
    first_number = float(input("Enter the number:\t"))

    # keep running the program until user want to see the result.
    result = None
    while True:

        # Printing the supported operations
        for operator in Db.OPERATORS:
            print(operator)

        # User's input
        requested_operation = input("Enter the operation you need to perform:"
                                    " or any key to see the result\t")

        # Check the request operation is valid if not break the loop.
        if requested_operation not in Db.OPERATORS:
            break

        next_number = float(input("Enter the next number:\t"))

        # Fetch the Method name based on the operation.
        calculation = Db.OPERATORS[requested_operation]

        # Call the function with respective values.
        # Takes first number, very first time.
        # After that, it takes a result as input variable.
        result = calculation(first_number if result is None else result, next_number)

        print(f"'{first_number if result is None else result}' {requested_operation} '{next_number}' = {result} ")
