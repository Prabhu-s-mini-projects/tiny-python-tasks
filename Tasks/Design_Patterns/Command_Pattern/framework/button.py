"""
Class Name: Button.py
Blue+print of:Button in GUI
"""
# Internal Dependencies
from Tasks.Design_Patterns.Command_Pattern.framework.command import Command


class Button:
    """
    Purpose: Blueprint of Button in GUI
    Attributes:
        label : str
        command : Command
    Methods:
        click : control will come here when a user clicks a button
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            label : str
        """
        self.label: str = kwargs.get("label")
        self.command: Command = kwargs.get("command")

    def click(self) -> None:
        """ To perform: control will come here when a user clicks a button"""
        self.command.execute()

    def disable(self) -> None:
        """ To perform: control will come here when a user clicks a button"""
        self.command.disable()
