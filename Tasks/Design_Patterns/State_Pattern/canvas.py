"""
Class Name: Canvas.py
Blue+print of:Canvas that used to draw an image
"""
# Internal Dependencies
from tool import Tool

# CONSTANTS
# TOOLS = {
#     'SELECTION': 'SELECTION',
#     'BRUSH':'BRUSH',
#     'ERASER': 'ERASER'
# }
class Canvas:
    """
    Purpose: Blueprint of Canvas that used to draw an image
    Attributes:
        current_tool : str
    Methods:
        mouse_down : action performed when the mouse was down
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            selected_tool : str
        """
        self.current_tool: Tool = kwargs.get("selected_tool")

    def mouse_down(self) -> None:
        """ To perform: action performed when the mouse was down"""

        # Below-mentioned code contains multiple if statement.
        # Will get more complex when we add a new state
        # if self.current_tool == TOOLS.get('SELECTION'):
        #     print("Selection")
        # elif self.current_tool ==TOOLS.get("BRUSH"):
        #     print("brush")
        # elif self.current_tool== TOOLS.get('ERASER'):
        #     print( "Eraser")

        self.current_tool.mouse_down()

    def mouse_up(self) -> None:
        """ To perform: action performed when the mouse was down"""

        # Also, we need to add new code every method.
        # here state pattern plays a major role
        # if self.current_tool == TOOLS.get('SELECTION'):
        #     print("draw rectangle")
        # elif self.current_tool == TOOLS.get("BRUSH"):
        #     print("painted using brush ")
        # elif self.current_tool == TOOLS.get('ERASER'):
        #     print("Erasered the canvas")

        self.current_tool.mouse_up()
