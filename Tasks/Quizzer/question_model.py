"""Contains the question class"""

class Question:
    """represent a question object with attributes of text and answer"""

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def q_text(self) -> None:
        """print question"""
        print(f"{ self.text = } ")

    def q_answer(self) -> None:
        """print question"""
        print(f"{ self.answer = } ")
