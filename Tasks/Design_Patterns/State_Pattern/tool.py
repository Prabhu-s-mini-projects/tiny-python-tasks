"""
Class Name: tool.py
Blue+print of:its is an abstract class to implement the state pattern
"""

# Dependencies
from abc import ABC, abstractmethod


# Internal Dependencies

# CONSTANTS

class Tool(ABC):
    """
    Purpose: Blueprint of its is an abstract class to implement the state pattern

    Methods:
        mouse_down :
        mouse_up:
    """

    @abstractmethod
    def mouse_down(self) -> None:
        """ To perform: """

    @abstractmethod
    def mouse_up(self) -> None:
        """ To perform: """
