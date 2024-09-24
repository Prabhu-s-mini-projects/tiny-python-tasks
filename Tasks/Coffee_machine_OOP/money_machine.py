""" Contains Money class"""
class MoneyMachine:
    """ Contains operational methods related to money"""
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self)-> None:
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self)-> float:
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES.items():
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost:float)-> bool:
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True

        # Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
        print("Sorry that's not enough money. Money refunded.")
        self.money_received = 0
        return False
