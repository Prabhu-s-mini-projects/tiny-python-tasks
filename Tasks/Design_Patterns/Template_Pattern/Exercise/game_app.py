"""
Class Name: GameAPPWindow.py
Blue+print of:inherits the window
"""
# Internal Dependencies
from Tasks.Design_Patterns.Template_Pattern.Exercise.window import Window


class GameAPPWindow(Window):
    """
    Purpose: Blueprint of inherits the window
    Methods:
        _before_closing : steps to follow before closing
    """

    def step1(self) -> None:
        """step1"""
        print("step:1")

    def step2(self) -> None:
        """step1"""
        print("step:2")

    def _before_closing(self) -> None:
        """ To perform: steps to follow before closing"""
        print("performing steps that need done before closing")
        self.step1()

    def _after_closing(self) -> None:
        """ To perform: steps to follow before closing"""
        print("Performing steps that need done before closing")
        self.step2()
