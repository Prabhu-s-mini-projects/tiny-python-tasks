"""
Class Name: History.py
Blue+print of:Contains the History for all new contents added in the editor
"""

# Internal Dependencies
from Tasks.Design_Patterns.Memento_Pattern.editor_state import EditorState


class History:
    """
    Purpose: Blueprint of Contains the History for all new contents added in the editor
    Attributes:
        states : list
    Methods:
        push : adds the new state
    """

    def __init__(self):
        """
        Attributes: states : list
        """
        self.states: list = []

    def push(self, new_state: EditorState) -> None:
        """ To perform: adds the new state"""
        self.states.append(new_state)

    def pop(self) -> EditorState:
        """pops the last element from the list"""
        return self.states.pop()
