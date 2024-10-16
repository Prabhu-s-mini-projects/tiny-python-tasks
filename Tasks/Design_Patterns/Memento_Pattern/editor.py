"""
Class Name: Editor.py
Blue+print of:Allows user to create and edit contents
"""

# Internal Dependencies
from Tasks.Design_Patterns.Memento_Pattern.editor_state import EditorState


class Editor:
    """
    Purpose: Blueprint of Allows user to create and edit contents
    Attributes:
        _content : str
    Methods:
        edit_content : allow user to edit contents
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            contents : str
        """
        self._content: str = kwargs.get("contents", "")

    @property
    def content(self) -> str:
        """ getter method for contents."""
        return self._content

    @content.setter
    def content(self, new_content: str) -> None:
        """ Setter method for contents."""
        self._content = new_content

    def create_state(self) -> EditorState:
        """Creates a new EDITOR state and adds into a history"""
        return EditorState(content=self._content)

    def restore(self, state: EditorState) -> None:
        """ Gets the previous values"""
        self._content = state.content
