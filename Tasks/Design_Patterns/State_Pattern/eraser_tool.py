"""
Class Name: Eraser_tool.py
Blue+print of:in-herites the Tool abstract class
"""
# Internal Dependencies
from tool import Tool


# CONSTANTS

class EraserTool(Tool):
    """
    Purpose: Blueprint of in-herites the Tool abstract class

    Methods:
        Override abstract super methods :
    """

    def mouse_down(self) -> None:
        """ Changes the cursor"""
        print("Eraser icon ")

    def mouse_up(self) -> None:
        """Implements the action of the selected tool"""
        print("Erased the canvas")
