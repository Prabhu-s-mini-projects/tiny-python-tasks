"""
Class Name: UndoCommand.py
Blue+print of:will execute an undo command
"""
# Internal Dependencies
from Tasks.Design_Patterns.Command_Pattern.Editor.framework.command import Command
from Tasks.Design_Patterns.Command_Pattern.Editor.history import History


class UndoCommand(Command):
    """
    Purpose: Blueprint of will execute an undo command
    Methods:
        execute : will execute the steps to undo a command
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            prev_content : str
            html_content: HtmlDocument
        """
        super().__init__()
        self.history: History = kwargs.get("history")

    def execute(self) -> None:
        """ To perform: will execute the steps to undo a command"""
        self.history.pop().execute()
