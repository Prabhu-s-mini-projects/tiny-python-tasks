"""
App_Name: Memento Pattern
Purpose: Examples of Memento Pattern
"""
from Tasks.Design_Patterns.Memento_Pattern.editor import Editor
from Tasks.Design_Patterns.Memento_Pattern.history import History


# Dependencies

# Internal modules

# CONSTANTS

# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Memento Pattern
    to do Examples of Memento Pattern
    """
    # To do
    print(
        """
        Memento Pattern:
        It's a behavioral design pattern that
        lets you save and restore the previous state of an object
        without revealing the details of its implementation.
        """
    )
    editor = Editor()
    history = History()

    editor.content = "a"
    history.push(editor.create_state())
    print(editor.content)

    editor.content = "b"
    history.push(editor.create_state())
    print(editor.content)

    editor.content = "c"
    print(editor.content)

    editor.restore(history.pop())
    print(editor.content)


if __name__ == '__main__':
    main()
