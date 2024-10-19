"""
Class Name: ChatClient.py
Blue+print of:encrypt the message and send the messages
"""
# Internal Dependencies
from Tasks.Design_Patterns.Strategy_Pattern.Exercise.ads_encryption import ADSAlgorithm


class ChatClient:
    """
    Purpose: Blueprint of encrypt the message and send the messages
    Attributes:
        encryption_algorithm : str
    Methods:
         send: send the message after encrypting
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            encryption_algorithm : str
        """
        self.encryption_algorithm: str = kwargs.get("encryption_algorithm")

    def send(self, message: str) -> None:
        """ To perform: encryption and send the command"""
        encryption = ADSAlgorithm()
        encryption.encrypt()
        print(f"{ self.encryption_algorithm = } ")

        # replace by above strategy pattern approach
        # if self.encryption_algorithm =="DES":
        #     print ("Encrypting the message using DES algorithm")
        # elif self.encryption_algorithm == "ADS":
        #     print("Encrypting the message using ADS")
        # else:
        #     print("Error")

        print(f"Sending the encrypted message... {message}")

    def receive(self, message: str) -> None:
        """ To perform: encryption and send the command"""
        decryption = ADSAlgorithm()
        decryption.decrypt()
        print(f"{ self.encryption_algorithm = } ")
        # replace by above strategy pattern approach
        # if self.encryption_algorithm =="DES":
        #     print ("Encrypting the message using DES algorithm")
        # elif self.encryption_algorithm == "ADS":
        #     print("Encrypting the message using ADS")
        # else:
        #     print("Error")

        print(f"Sending the encrypted message... {message}")
