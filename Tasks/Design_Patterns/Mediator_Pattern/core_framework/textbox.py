"""
Class Name: TextBox.py
Blue+print of:UI control Text box
"""
# Dependencies

# Internal Dependencies
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.ui_control import UIControl

# CONSTANTS

class TextBox(UIControl): # [too-few-public-methods]
    """
    Purpose: Blueprint of UI control Text box
    Attributes:
        _content : str
    Methods:
        get_value : a fake method
        set_value: a fake method
    """

    def __init__(self, **kwargs):
        """
        Recommend using kwargs
        Attributes:
            value : str
        """
        super().__init__(**kwargs)
        self._content: str = kwargs.get("content")

    @property
    def content(self) -> str:
        """ To perform: a fake get method"""
        return  self._content

    @content.setter
    def content(self, content) -> None:
        """ To perform: a fake set method
        :type content: object
        """
        self._content = content
        self.owner.changed(ui_control=self)
