"""
Class Name: EditorState.py
Blue+print of:Creates the contents of that particular state
"""


class EditorState:
    """
    Purpose: Blueprint of Creates the contents of that particular state
    Attributes:
        _content : str
    """

    def __init__(self, **kwargs):
        """
        Recommend to use kwargs
        Attributes:
            content : str
        """
        self._content: str = kwargs.get("content")

    @property
    def content(self) -> str:
        """ getter method for contents."""
        return self._content

    @content.setter
    def content(self, new_content: str) -> None:
        """ Setter method for contents."""
        self._content = new_content

    def print_doc_(self) -> None:
        """print doc string for pylint fix """
        print("ignore this method")
