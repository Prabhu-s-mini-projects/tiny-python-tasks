from Menu import Menu
from Coffee_Maker import CoffeeMaker
from Money_Machine import MoneyMachine

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