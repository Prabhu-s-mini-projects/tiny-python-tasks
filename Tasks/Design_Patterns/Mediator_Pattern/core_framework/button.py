"""
Class Name: Button.py
Blue+print of: UI control of button
"""
# Dependencies

# Internal Dependencies
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.ui_control import UIControl

# CONSTANTS

class Button(UIControl): # [too-few-public-methods]
    """
    Purpose: Blueprint of UI control Text box
    Attributes:
        _is_enabled : bool
    Methods:
        get_value : a fake method
        set_value: a fake method
    """

    def __init__(self, **kwargs):
        """
        Recommend using kwargs
        Attributes:
            value : bool
        """
        super().__init__(**kwargs)
        self._is_enabled: bool = kwargs.get("is_enabled")

    @property
    def is_enabled(self) -> bool:
        """ To perform: a fake get method"""
        return  self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled: bool) -> None:
        """ To perform: a fake set method"""
        self._is_enabled = is_enabled
        self.owner.changed(ui_control=self)
