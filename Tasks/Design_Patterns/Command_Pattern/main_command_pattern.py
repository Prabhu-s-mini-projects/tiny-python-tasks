"""
App_Name: Command pattern
Purpose: access the object/class that implement the command pattern
"""  # Internal modules
from Tasks.Design_Patterns.Command_Pattern.add_customer_command import AddCustomerCommand
from Tasks.Design_Patterns.Command_Pattern.apply_bw_filter_command import BWFilter
from Tasks.Design_Patterns.Command_Pattern.composite_command import CompositeCommand
from Tasks.Design_Patterns.Command_Pattern.customer_services import CustomerService
from Tasks.Design_Patterns.Command_Pattern.framework.button import Button
from Tasks.Design_Patterns.Command_Pattern.resize_command import ResizeCommand


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Command pattern
    to do access the object/class that implement the command pattern
    """
    # To do
    print(
        """
        Command Pattern:
        it's a behavioral design pattern that turns a request into a stand-alone object,
        that contains all information about the request.
        This transformation lets you pass requests as a method arguments, 
        delay or queue a request’s execution, and support undoable operations.
        """
    )

    customer_service = CustomerService()
    add_customer = AddCustomerCommand(customer_service=customer_service)
    add_button = Button(command=add_customer)
    add_button.click()

    composite_command = CompositeCommand()
    composite_command.add(ResizeCommand())
    composite_command.add(BWFilter())

    composite_command.execute()
    composite_command.execute()
    composite_command.execute()
    composite_command.execute()


if __name__ == '__main__':
    main()
