"""
Class Name: Encryption.py
Blue+print of:Abstract class for all types of encryption
"""
# Dependencies
from abc import ABC, abstractmethod


class Encryption(ABC):
    """
    Purpose: Blueprint of Abstract class for all types of encryption
    Methods:
        encrypt : will encrypt based on the type
        decrypt: will decrypt the message
    """

    @abstractmethod
    def encrypt(self) -> None:
        """ To perform: will encrypt based on the type"""

    @abstractmethod
    def decrypt(self) -> None:
        """will decrypt the message"""
