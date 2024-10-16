"""
Class Name: DocumentState.py
Blue+print of:Create an object state at the time of creation
"""


class DocumentState:
    """
    Purpose: Blueprint of Create an object state at the time of creation
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

    @property
    def font_name(self) -> str:
        """ getter method for contents."""
        return self._font_name

    @property
    def font_size(self) -> str:
        """ getter method for contents."""
        return self._font_size
