import Database as Db

# Loading the calculator
print(Db.logo)

# Get user input:
first_number = float(input("Enter the number:\t"))

# keep running the program until user want to see the result.
result = None
while True:

    # Printing the supported operations
    for operator in Db.operators:
        print(operator)

    # User's input
    requested_operation = input("Enter the operation you need to perform: or any key to see the result\t")

    # Check the request operation is valid if not break the loop.
    if requested_operation not in Db.operators:
        break
    else:
        next_number = float(input("Enter the next number:\t"))

    # Fetch the Method name based on the operation.
    calculation = Db.operators[requested_operation]

    # Call the function with respective values.
    # takes first number, very first time. after that it takes result as input variable.
    result = calculation(first_number if result is None else result, next_number)

    print(f"'{first_number if result is None else result}' {requested_operation} '{next_number}' = {result} ")
