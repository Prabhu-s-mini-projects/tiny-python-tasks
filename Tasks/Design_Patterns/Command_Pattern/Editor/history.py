"""
Class Name: History.py
Blue+print of:will contain a list of commands
"""
from Tasks.Design_Patterns.Command_Pattern.Editor.framework.command import Command


# Dependencies

# Internal Dependencies

# CONSTANTS

class History:
    """
    Purpose: Blueprint of will contain a list of commands
    Attributes:
        command_history : list
    Methods:
        push : will add it to the list
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            command_history : list
        """
        self.command_history: list = kwargs.get("command_history") \
            if kwargs.get("command_history") is not None else []

    def push(self, command: Command) -> None:
        """ To perform: will add it to the list"""
        self.command_history.append(command)

    def pop(self) -> Command:
        """ To perform: will add it to the list"""
        return self.command_history.pop() if len(self.command_history) > 0 else ""
