import Coffee_Machine_Database as Db

# Load data from Database
menu = Db.MENU
resources = Db.RESOURCES
money_in_bank: float = 0.00


def load_logo() -> None:
    print(Db.LOGO)


# # Todo:3
def report() -> None:
    """
     To display current quantity of Resources.
    """
    print(f"Water : {resources.get('water')}ml")
    print(f"Milk : {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print(f"Money : ${money_in_bank}")


def is_valid(user_ask):
    return user_ask in menu or user_ask in ['report', 'off']


# # Todo:4
def is_resources_sufficient(order: dict) -> bool:
    """
    To check whether we have a sufficient resources to make a respective coffee.
    """
    needed_ingredients = order.get('ingredients')
    for ingredient in needed_ingredients:
        if resources.get(ingredient) < needed_ingredients.get(ingredient):
            # if resources is not sufficient "Sorry there is not enough respective resources"
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


# # Todo:5
def process_coins() -> float:
    """
    calculate the amount based on the pennies , Dimes, Quarters & nickels
    :return: Total amount
    """
    total = 0.0
    total += int(input("how many quarters?:\t")) * Db.DOMINATION.get("quarters")
    total += int(input("how many dimes?:\t")) * Db.DOMINATION.get("dimes")
    total += int(input("how many nickles?:\t")) * Db.DOMINATION.get("nickles")
    total += int(input("how many pennies?:\t")) * Db.DOMINATION.get("pennies")
    return total


# # Todo:6
def is_transaction_successful(order_amount, payment) -> bool:
    """
    Checks whether inserted coins is sufficient for the Order cost
    """
    if payment > order_amount:
        print(f"here is the change : {payment-order_amount}")
        return True
    elif payment == order_amount:
        return True
    return False


# # Todo:7
def make_order(order):
    """
    # Make Coffee
    """

    # Using the ingredients to make a coffee
    needed_ingredients = order.get('ingredients')
    for ingredient in needed_ingredients:
        resources[ingredient] = resources.get(ingredient) - needed_ingredients.get(ingredient)

    print(order.get('serve'))

    print("After purchasing")
    report()


def perform_task(user_ask) -> bool:
    if user_ask in menu:

        order = menu.get(user_ask)

        if is_resources_sufficient(order):

            payment = process_coins()

            if is_transaction_successful(order.get('cost'), payment):

                print(f"Before purchasing {user_ask}")
                report()

                global money_in_bank
                money_in_bank += order.get('cost')

                make_order(order)

            else:

                print(f"Order Cost : {order.get('cost')}.\n Money Inserted: {payment}.")
                print("Sorry that's not enough money. Money refunded.")

    elif user_ask == "report":

        report()

    else:
        # Indicates all possibility are check. User_ask is to OFF
        # # Todo:2
        # Create a method to exit the loop and update machine_state as off
        return False

    return True
