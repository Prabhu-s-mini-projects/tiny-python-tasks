"""
App_Name: state Pattern
Purpose: Example of a state-pattern
"""
from Tasks.Design_Patterns.State_Pattern.brush_tool import BrushTool
from Tasks.Design_Patterns.State_Pattern.canvas import Canvas
from Tasks.Design_Patterns.State_Pattern.eraser_tool import EraserTool
from Tasks.Design_Patterns.State_Pattern.section_tool import SelectionTool


# Internal modules


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : state Pattern
    to do Example of a state pattern
    """
    # To do
    canvas =  Canvas()
    
    canvas.current_tool = SelectionTool()
    canvas.mouse_down()
    canvas.mouse_up()

    canvas.current_tool = BrushTool()
    canvas.mouse_down()
    canvas.mouse_up()

    canvas.current_tool = EraserTool()
    canvas.mouse_down()
    canvas.mouse_up()


if __name__ == '__main__':
    main()
