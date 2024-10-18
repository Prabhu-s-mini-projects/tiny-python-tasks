"""
Class Name: TravelMode.py
Blue+print of:Travel_Mode, and it inherits Abstract class
"""
# Dependencies
from abc import ABC, abstractmethod


class TravelMode(ABC):
    """
    Purpose: Blueprint of Travel_Mode, and it inherits abstract class
    """

    @abstractmethod
    def get_eta(self) -> int:
        """Abstract method implementation will be in inherited class """

    @abstractmethod
    def get_direction(self) -> int:
        """Abstract method implementation will be in inherited class """
