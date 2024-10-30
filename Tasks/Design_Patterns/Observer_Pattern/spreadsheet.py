"""
Class Name: SpreadSheet.py
Blue+print of:contain a value inside a table that depend on observer
"""
# Internal Dependencies
from Tasks.Design_Patterns.Observer_Pattern.observer import Observer

class SpreadSheet(Observer):
    """
    Purpose: Blueprint of contain a value inside a table that depend on observer
    Attributes:
        total : int
    Methods:
        calculate_sum : adds 5 to value from data sources
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            total : int
        """
        self.total: int = kwargs.get("total")
        self.value_from_dataSource = self.update()

    def calculate_sum(self) -> None:
        """ To perform: adds 5 to value from data sources"""
        self.total = self.value_from_dataSource

    def update(self) -> int:
        """ updates the value in a spreadsheet"""
        print("spreadsheet value is updated")
        return 0
