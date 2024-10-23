"""
Class Name: BoldCommand.py
Blue+print of:will bold the contents
"""
# Internal Dependencies
from Tasks.Design_Patterns.Command_Pattern.Editor.framework.undoable_command import UndoableCommand
from Tasks.Design_Patterns.Command_Pattern.Editor.history import History
from Tasks.Design_Patterns.Command_Pattern.Editor.html_document import HtmlDocument


class BoldCommand(UndoableCommand):
    """
    Purpose: Blueprint of will bold the contents
    Attributes:
        prev_content : str
        html_content: HtmlDocument
        history: History
    Methods:
        execute : will make the content bold
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            prev_content : str
            html_content: HtmlDocument
        """
        super().__init__()
        self.html_content: HtmlDocument = kwargs.get("html_content")
        self.history: History = kwargs.get("history")
        self.prev_content: str = ""

    def execute(self) -> None:
        """ To perform: will make the content bold"""
        self.prev_content = self.html_content.content
        self.html_content.make_bold()
        self.history.push(self)

    def un_execute(self) -> None:
        """ To perform: will make the content bold"""
        self.html_content.content = self.prev_content
