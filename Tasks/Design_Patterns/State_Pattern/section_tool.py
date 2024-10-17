"""
Class Name: SelectionTool.py
Blue+print of:in-herites the Tool abstract class
"""
# Internal Dependencies
from tool import Tool


# CONSTANTS

class SelectionTool(Tool):
    """
    Purpose: Blueprint of in-herites the Tool abstract class

    Methods:
        Override abstract super methods :
    """

    def mouse_down(self) -> None:
        """ Changes the cursor"""
        print("Selection icon ")

    def mouse_up(self) -> None:
        """Implements the action of the selected tool"""
        print("Draw a rectangle ")
