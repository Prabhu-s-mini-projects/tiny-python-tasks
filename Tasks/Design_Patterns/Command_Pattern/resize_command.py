"""
Class Name: ResizeCommand.py
Blue+print of:will resize the image when we execute the command
"""
# Internal Dependencies
from Tasks.Design_Patterns.Command_Pattern.framework.command import Command


class ResizeCommand(Command):
    """
    Purpose: Blueprint of will resize the image when we execute the command
    Methods:
         execute: Resized the image
    """

    def execute(self) -> None:
        """ To perform: Resized the image """
        print("Resized the image")

    def disable(self) -> None:
        """ To perform: Resized the image option disabled"""
        print("Resized the image option disabled")
