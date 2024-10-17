""" Contains question class"""
class Question:
    """Contains question class"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def question(self) -> None:
        """print question"""
        print(f"{ self.question = } ")

    def answer(self) -> None:
        """print question"""
        print(f"{ self.answer = } ")
