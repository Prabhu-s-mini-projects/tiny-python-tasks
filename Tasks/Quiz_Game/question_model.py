""" Contains question class"""
class Question:
    """Contains question class"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def q_question(self) -> None:
        """print question"""
        print(f"{ self.question = } ")

    def a_answer(self) -> None:
        """print question"""
        print(f"{ self.answer = } ")
