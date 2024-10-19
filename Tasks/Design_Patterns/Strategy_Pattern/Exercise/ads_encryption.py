"""
Class Name: ADSAlgorithm.py
Blue+print of:will encrypt the message using ads algo
"""
# Internal Dependencies
from Tasks.Design_Patterns.Strategy_Pattern.Exercise.encryption import Encryption


class ADSAlgorithm(Encryption):
    """
    Purpose: Blueprint of will encrypt the message using ads algo

    Methods:
        encrypt : Encrypt using ADS
    """

    def encrypt(self) -> None:
        """ To perform: Encrypt using ADS"""
        print("Encrypting the message using ADS algorithm")

    def decrypt(self) -> None:
        """ To perform: Encrypt using ADS"""
        print("decrypting the message using ADS algorithm")
