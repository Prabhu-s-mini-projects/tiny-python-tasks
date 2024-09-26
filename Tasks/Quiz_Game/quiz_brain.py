"""Contains Quiz brains class"""
class QuizBrain:
    """act as interfacer between data and quiz"""

    def __init__(self, question_bank: list):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self)-> None:
        """Reads next question"""
        player_answer = input(f"Q.{self.question_number+1}:"
                              f"{self.question_list[self.question_number].question}?"
                              f" (True/False) :\t").lower()
        self.validate_answer(player_answer, self.question_list[self.question_number].answer.lower())
        self.question_number += 1

    def still_has_questions(self)-> bool:
        """Check whether we have a next question"""
        return self.question_number < len(self.question_list)

    def validate_answer(self, player_answer: str, correct_answer: str)-> None:
        """ Checks answer with user response"""
        if player_answer == correct_answer:
            print("You got it right")
            self.score += 1
        else:
            print("That's Wrong.\n")
