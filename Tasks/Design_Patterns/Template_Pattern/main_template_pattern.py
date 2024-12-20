"""
App_Name: Template_Pattern
Purpose: Will provide an example for Template Pattern using Audit class as an example
"""  # Internal modules
from Tasks.Design_Patterns.Template_Pattern.generate_report import GenerateReport
from Tasks.Design_Patterns.Template_Pattern.transfer_money import TransferMoney


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Template_Pattern
    to do Will provide an example for Template Pattern using Audit class as an example
    """
    # To do :
    print(
        """
        Template Method:
        It's a behavioral design pattern that
        defines the skeleton of an algorithm in the superclass,
        but, lets subclasses override specific steps of the algorithm
        without changing its structure.
        """
    )

    # Here is a scenario.
    # In a bank, We need to record all the tasks that are performed.
    # So Every task class should have a Recoder object.
    # Before executing every task recoder object should record.
    # The Above-mentioned steps should follow for every new task.

    task = TransferMoney()
    task.execute()

    task = GenerateReport()
    task.execute()


if __name__ == '__main__':
    main()
