"""Contains 2 class MenuItem and Menu Class"""
class MenuItem:
    """Models each Menu Item."""

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.cost = kwargs.get('cost')
        self.ingredients = {
            "water": kwargs.get('water'),
            "milk": kwargs.get('milk'),
            "coffee": kwargs.get('coffee')
        }

    def required_ingredients(self) -> None:
        """ prints the required ingredients"""
        print(f"{ self.ingredients = } ")

    def print_details(self) -> None:
        """print all the variables """
        print(f"{ self.name = } ")
        print(self.ingredients)
        print(f"{ self.cost = } ")

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self)-> str:
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name: str) -> MenuItem | None:
        """
        Searches the menu for a particular drink by name.
        Returns that item if it exists, otherwise returns None
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None
