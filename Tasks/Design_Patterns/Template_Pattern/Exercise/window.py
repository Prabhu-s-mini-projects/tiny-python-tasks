"""
Class Name: Window.py
Blue+print of:window in GUI framework
"""
# Dependencies
from abc import ABC, abstractmethod


class Window(ABC):
    """
    Purpose: Blueprint of a window in GUI framework
    Methods:
         open: To open a window
         close: To close a window
    """

    def open(self) -> None:
        """To close a window: """
        print(" opening an window")

    def close(self) -> None:
        """ To perform: """
        self._before_closing()
        print(" closing an window")
        self._after_closing()

    @abstractmethod
    def _before_closing(self) -> None:
        """before closing"""

    @abstractmethod
    def _after_closing(self) -> None:
        """after closing"""
