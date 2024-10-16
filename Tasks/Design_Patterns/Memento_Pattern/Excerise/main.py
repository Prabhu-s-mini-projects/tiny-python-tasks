"""
App_Name: Exercise app for Memento pattern
Purpose: allow user to add and delete content in the document
"""
from Tasks.Design_Patterns.Memento_Pattern.Excerise.document import Document
from Tasks.Design_Patterns.Memento_Pattern.Excerise.history import History


# Internal modules


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Exercise app for Memento Pattern
    to do allow user to add and delete content in the document
    """
    # To do
    document = Document()
    history = History()

    document.content = "a"
    history.push(document.create_state())
    print(f"{ document.content = } ")
    print(f"{ document.font_name = } ")
    print(f"{ document.font_size = } ")

    document.font_name = "courier"
    history.push(document.create_state())
    print(f"{ document.content = } ")
    print(f"{ document.font_name = } ")
    print(f"{ document.font_size = } ")

    document.font_size = "10"
    history.push(document.create_state())
    print(f"{ document.content = } ")
    print(f"{ document.font_name = } ")
    print(f"{ document.font_size = } ")

    document.content = "b"
    # history.push(document.create_state())
    print(f"{ document.content = } ")
    print(f"{ document.font_name = } ")
    print(f"{ document.font_size = } ")

    print("after restore")
    document.restore(history.pop())
    print(f"{ document.content = } ")
    print(f"{ document.font_name = } ")
    print(f"{ document.font_size = } ")

if __name__ == '__main__':
    main()
