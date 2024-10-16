"""
Class Name: Document.py
Blue+print of:all user to add content in the document
"""
# Internal Dependencies
from Tasks.Design_Patterns.Memento_Pattern.Excerise.document_state import DocumentState

class Document:
    """
    Purpose: Blueprint of all users to add content in the document
    Attributes:
        _content : str
    Methods:
        create_state : creates a state of the object
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            _content : str
            _font_name: str
            _font_size: int
        """
        self._content: str = kwargs.get("content", "")
        self._font_name: str = kwargs.get("font_name", "")
        self._font_size: str = kwargs.get("font_size", "")

    @property
    def content(self) -> str:
        """ getter method for contents."""
        return self._content

    @content.setter
    def content(self, new_content: str) -> None:
        """ Setter method for contents."""
        self._content = new_content

    @property
    def font_name(self) -> str:
        """ getter method for contents."""
        return self._font_name

    @font_name.setter
    def font_name(self, font_name: str) -> None:
        """ Setter method for contents."""
        self._font_name = font_name

    @property
    def font_size(self) -> str:
        """ getter method for contents."""
        return self._font_size

    @font_size.setter
    def font_size(self, font_size: str) -> None:
        """ Setter method for contents."""
        self._font_size = font_size

    def create_state(self) -> DocumentState:
        """ To perform: creates a state of the object"""
        return DocumentState(
            font_size=self._font_size,
            font_name=self._font_name,
            content=self._content
        )

    def restore(self, state: DocumentState) -> None:
        """ reassign the value to restore state"""
        self._content = state.content
        self._font_name = state.font_name
        self._font_size = state.font_size
