"""
Class Name: Observer.py
Blue+print of:abstract class to implement an obsever
"""
# Dependencies
from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Purpose: Blueprint of abstract class to implement an obsever
    Methods:
        update : Updates a new value
    """

    @abstractmethod
    def update(self) -> None:
        """ To perform: Updates a new value"""
