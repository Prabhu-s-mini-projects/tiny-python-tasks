"""
Class Name: AddCustomerCommand.py
Blue+print of:implements the method of abc command class
"""
from Tasks.Design_Patterns.Command_Pattern.customer_services import CustomerService
# Internal Dependencies
from Tasks.Design_Patterns.Command_Pattern.framework.command import Command


class AddCustomerCommand(Command):
    """
    Purpose: Blueprint of implements the method of abc command class
    Methods:
        execute : will implement the steps to take when command execute is called
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            label : str
        """
        self.customer_service: CustomerService = kwargs.get("customer_service")

    def execute(self) -> None:
        """will implement the steps to take when command execute is called"""
        self.customer_service.add_customer()

    def disable(self) -> None:
        """will implement the steps to take when command execute is called"""
        print("Customer added option disabled")
