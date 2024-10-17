"""
Class Name: Canvas.py
Blue+print of:Canvas that used to draw an image
"""


# Internal Dependencies

# CONSTANTS

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
        self.current_tool: str = kwargs.get("selected_tool")

    def mouse_down(self) -> None:
        """ To perform: action performed when the mouse was down"""
        pass

    def mouse_up(self) -> None:
        """ To perform: action performed when the mouse was down"""
        pass
