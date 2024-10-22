"""
Class Name: Command.py
Blue+print of:convert request into objects
"""
# Dependencies
from abc import ABC, abstractmethod


class Command(ABC):
    """
    Purpose: Blueprint of convert request into objects
    Methods:
        execute : Will implement what to what the command is called
    """

    @abstractmethod
    def execute(self) -> None:
        """ To perform: Will implement what to do the command is called"""

    @abstractmethod
    def disable(self) -> None:
        """ To perform: Will implement what to do command is called"""
