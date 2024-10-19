""" 
App_Name: ChatClient
Purpose: Exercise of a Strategy patten
"""
# Internal modules
from Tasks.Design_Patterns.Strategy_Pattern.Exercise.chat_client import ChatClient


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : ChatClient
    to do Exercise of a Strategy patten
    """
    # To do
    chat_client = ChatClient()

    chat_client.encryption_algorithm = 'ADS'
    chat_client.send("here is the message")


if __name__ == '__main__':
    main()
