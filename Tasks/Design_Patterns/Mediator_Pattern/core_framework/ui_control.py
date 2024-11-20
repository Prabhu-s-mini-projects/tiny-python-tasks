"""
Class Name: UIControl.py
Blue+print of:Contains all other UI tools
"""
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.dialog_box import DialogBox


# Dependencies

# Internal Dependencies
# CONSTANTS

class UIControl:
    """
    Purpose: Blueprint of Contains all other UI tools
    Attributes:
        owner : DialogBox
    Methods:
        _get_owner : will return Owner a fake method
    """

    def __init__(self, **kwargs):
        """
        Recommend to use kwargs
        Attributes:
            _owner : DialogBox
        """
        self.owner: DialogBox = kwargs.get("owner")

    def _get_owner(self) -> None:
        """ To perform: will return Owner dummy method"""
        pass
