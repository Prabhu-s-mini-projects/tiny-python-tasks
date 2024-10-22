"""
Class Name: CompositeCommand.py
Blue+print of:collects a bunch of commands and execute in the same order
"""
from Tasks.Design_Patterns.Command_Pattern.framework.command import Command


# Dependencies

# Internal Dependencies

# CONSTANTS

class CompositeCommand:
    """
    Purpose: Blueprint of collects a bunch of commands and execute in same order
    Attributes:
        commands : list
    Methods:
        execute : Will execute all the command in commands
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            commands : list
        """
        self.commands: list = kwargs.get("commands") if kwargs.get("commands") is not None else []

    def add(self, command: Command) -> None:
        """Will add the command request object"""
        self.commands.append(command)

    def execute(self) -> None:
        """ To perform: Will execute all the command in commands"""
        for command in self.commands:
            command.execute()
