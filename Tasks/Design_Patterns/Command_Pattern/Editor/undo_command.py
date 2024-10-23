"""
Class Name: UndoCommand.py
Blue+print of:will execute an undo command
"""
# Internal Dependencies
from Tasks.Design_Patterns.Command_Pattern.Editor.framework.command import Command


class UndoCommand(Command):
    """
    Purpose: Blueprint of will execute an undo command
    Methods:
        execute : will execute the steps to undo a command
    """

    def execute(self) -> None:
        """ To perform: will execute the steps to undo a command"""
        pass
