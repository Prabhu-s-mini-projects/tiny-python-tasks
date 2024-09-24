""" Main or view file of coffee machines """
# Dependencies
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main()-> None:
    """ Contains the main loops of the program"""
    menu = Menu()
    coffee_maker = CoffeeMaker()
    bank = MoneyMachine()

    while True:
        request = input("What would you like? (espresso/latte/cappuccino/):\t").lower()
        if request == "report":
            coffee_maker.report()
        elif request =="off":
            break
        elif coffee_maker.is_resource_sufficient(drink=menu.find_drink(request)) and bank.make_payment(menu.find_drink(request).cost):
            coffee_maker.make_coffee(menu.find_drink(request))
        else:
            print(f"please enter valid input : {request} is not valid")

if __name__ == '__main__':
    main()