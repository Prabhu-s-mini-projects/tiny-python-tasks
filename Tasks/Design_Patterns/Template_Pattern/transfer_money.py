"""
Class Name: TransferMoney.py
Blue+print of:Transfer money in the bank
"""
# Internal Dependencies
from Tasks.Design_Patterns.Template_Pattern.tasks import Tasks


class TransferMoney(Tasks):
    """
    Purpose: Blueprint of Transfer money in the bank
    Methods:
        get_amount : print the amount involved in transaction
    """

    def get_amount(self) -> None:
        """ To perform: print the amount involved in transaction"""
        self._do_execute()

    def _do_execute(self) -> None:
        """ To perform: transferring the amount"""
        print("Transferring the amount")
