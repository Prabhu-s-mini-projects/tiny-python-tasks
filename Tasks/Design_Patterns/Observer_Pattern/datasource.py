"""
Class Name: DataSources.py
Blue+print of:Contain a data sources that contains data
"""
from Tasks.Design_Patterns.Observer_Pattern.subject import Subject


class DataSources(Subject):
    """
    Purpose: Blueprint of Contain a data sources that contains data
    Attributes:
        value : int
    Methods:
        print_value : will print the value of an object
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            value : int
        """
        super().__init__()
        self._value: int = kwargs.get("value")

    def print_value(self) -> None:
        """ To perform: will print the value of an object"""
        print(f"{self._value =}")

    @property
    def value(self)->int:
        """returns the private string"""
        return self._value

    @value.setter
    def value(self,value:int)-> None:
        """Todo: sets the value of an integer"""
        self._value = value
        self.notify()
