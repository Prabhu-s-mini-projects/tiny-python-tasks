"""
Class Name: AccessModifiers.py
Blue+print of:Documentation that defines how to declare access modifiers
"""


# Dependencies

# Internal Dependencies

# CONSTANTS

class AccessModifiers:
    """
    Purpose: Blueprint of Documentation that defines how to declare access modifiers
    Attributes:
        public_member : str     # By default all the members are public members
        _protected_member : str # Will/Should be access only to child and current class
        __private_member : str  # Access only inside a class
    Methods:
        __private_method : '__' indicates it's a private method or a members
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            public_member : str     # By default all the members are public members
            _protected_member : str # Will/Should be access only to child and current class
            __private_member : str  # Access only inside a class
        """
        self.public_member: str = kwargs.get("public_member")
        self._protected_member: str = kwargs.get("_protected_member")
        self.__private_member: str = kwargs.get("__private_member")

    def __private_method(self) -> None:
        """ To perform: '__' indicates it's a private method or a members"""
        print(f"Private Method that access {self.__private_member}")

    def _protected_method(self) -> None:
        """ To perform: '__' indicates it's a private method or a members"""
        print(f"_protected Method that can be access {self._protected_member}")

    def public_method(self) -> None:
        """ To perform: '__' indicates it's a private method or a members"""
        print(f"public Method that any one  {self.public_member}")
