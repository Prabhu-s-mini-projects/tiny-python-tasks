"""
Class Name: ListBox.py
Blue+print of:UI control Text box
"""
# Dependencies

# Internal Dependencies
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.ui_control import UIControl

# CONSTANTS

class ListBox(UIControl):
    """
    Purpose: Blueprint of UI control Text box
    Attributes:
        _selection : str
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
        self._selection: str = kwargs.get("selection")
    @property
    def selection(self) -> str:
        """ To perform: a fake get method"""
        return  self._selection

    @selection.setter
    def selection(self, selection) -> None:
        """ To perform: a fake set method"""
        self._selection = selection
        self.owner.changed(ui_control=self)
