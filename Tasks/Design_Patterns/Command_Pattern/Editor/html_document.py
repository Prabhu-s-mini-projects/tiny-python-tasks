"""
Class Name: HtmlDocument.py
Blue+print of:User will add the contents to the document.
"""


# Dependencies

# Internal Dependencies

# CONSTANTS

class HtmlDocument:
    """
    Purpose: Blueprint of User will add the contents to the document.
    Attributes:
        content : str
    Methods:
        make_bold : will make the contents bold
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            content : str
        """
        self.content: str = kwargs.get("content")

    def make_bold(self) -> None:
        """ To perform: will make the contents bold"""
        self.content = "<b>" + self.content + "</b>"

    def make_italic(self) -> None:
        """ To perform: will make the contents italic"""
        self.content = "<i>" + self.content + "</i>"
