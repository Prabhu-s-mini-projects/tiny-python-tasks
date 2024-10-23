"""
Class Name: UndoableCommand.py
Blue+print of:will execute the procedure to undo the previous command
"""
# Dependencies
from abc import abstractmethod

# Internal Dependencies
from Tasks.Design_Patterns.Command_Pattern.Editor.framework.command import Command


class UndoableCommand(Command):
    """
    Purpose: Blueprint of will execute the procedure to undo the previous command
    Methods:
        execute : will execute the steps to undo a command
    """

    @abstractmethod
    def un_execute(self) -> None:
        """ To perform: will execute the steps to undo a command"""

    @abstractmethod
    def dummy_method_2(self) -> None:
        """ To perform: will execute the steps to undo a command"""
