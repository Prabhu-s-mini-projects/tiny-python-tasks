"""
Class Name: DialogBox.py
Blue+print of:Will act as a mediator for various tools
"""
# Dependencies
from abc import  ABC, abstractmethod




class DialogBox(ABC):
    """
    Purpose: Blueprint of Will act as a mediator for various tools
    Methods:
        changed : Abstract method
    """
    @abstractmethod
    def changed(self, ui_control) -> None:
        """ To perform: Abstract method"""
