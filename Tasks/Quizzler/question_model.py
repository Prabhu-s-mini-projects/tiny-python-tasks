"""Contains the question class"""

class Question:
    """represent a question object with attributes of text and answer"""

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
