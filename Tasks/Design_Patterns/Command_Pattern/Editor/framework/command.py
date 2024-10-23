"""
Class Name: Command.py
Blue+print of:abstract class for command request
"""
# Dependencies
from abc import ABC, abstractmethod


class Command(ABC):
    """
    Purpose: Blueprint of abstract class for command request
    Attributes:
        prev_content : str
    Methods:
        execute : will execute the command
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            prev_content : str
        """
        self.prev_content: str = kwargs.get("prev_content")

    @abstractmethod
    def execute(self) -> None:
        """ To perform: will execute the command"""

    @abstractmethod
    def dummy_method(self) -> None:
        """ To perform: will execute the command"""
