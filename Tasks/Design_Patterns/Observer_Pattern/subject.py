"""
Class Name: Subject.py
Blue+print of:creates a subject
"""
# Dependencies
from Tasks.Design_Patterns.Observer_Pattern.observer import Observer

class Subject:
    """
    Purpose: Blueprint of creates a subject
    """

    def __init__(self):
        """
        Attributes:
            __observers : list
        """
        self.__observers: list = []

    # Observer Pattern[add Observer]
    def add_observer(self, obs: Observer) -> None:
        """will add the observer into an observer list"""
        if obs not in self.__observers:
            self.__observers.append(obs)
        else:
            print(f"{obs} is already an Observer")

    # Observer Pattern[remove Observer]
    def remove_observer(self, obs: object) -> None:
        """will add the observer into an observer list"""
        if obs in self.__observers:
            self.__observers.remove(obs)
        else:
            print(f"{obs} is not an Observer")

    # Observer Pattern[Notify Observers]
    def notify(self)-> None:
        """ Notify each and every observer"""
        for observer in self.__observers:
            observer.update()
