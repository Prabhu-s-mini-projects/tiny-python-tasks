"""
Class Name: BWFilter.py
Blue+print of:will apply black and white filter
"""
# Internal Dependencies
from Tasks.Design_Patterns.Command_Pattern.framework.command import Command


class BWFilter(Command):
    """
    Purpose: Blueprint of will apply black and white filter
    """

    def execute(self) -> None:
        """ To perform: Resized the image """
        print("BW filter applied to the image")

    def disable(self) -> None:
        """ To perform: Resized the image option disabled"""
        print("BW filter option disabled")
