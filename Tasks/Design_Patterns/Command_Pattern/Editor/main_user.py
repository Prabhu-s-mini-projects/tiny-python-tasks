"""
App_Name: Editing the HTML document
Purpose: allows user to edit and contents of aH TML file using the Undo-command pattern
"""
from Tasks.Design_Patterns.Command_Pattern.Editor.bold_command import BoldCommand
from Tasks.Design_Patterns.Command_Pattern.Editor.history import History
from Tasks.Design_Patterns.Command_Pattern.Editor.html_document import HtmlDocument
from Tasks.Design_Patterns.Command_Pattern.Editor.undo_command import UndoCommand


# Dependencies

# Internal modules

# CONSTANTS

# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Editing the HTML document
    to do allows user to edit and contents of aH TML file using the Undo-command pattern
    """
    # To do
    print(
        """
        The Main difference btw undo command pattern and memento pattern is 
        1. avoid using the history
        """
    )
    history = History()
    undo_command = UndoCommand(history=history)
    document = HtmlDocument()
    document.content = "hello World"

    bold_command = BoldCommand(history=history, html_content=document)
    bold_command.execute()
    print(f"{ document.content = } ")

    bold_command.un_execute()
    print(f"{ document.content = } ")

    bold_command.execute()
    print(f"{ document.content = } ")

    undo_command.execute()
    print(f"{ document.content = } ")


if __name__ == '__main__':
    main()
