""" View or Main entry of Quizzer application"""
import requests

from question_model import Question
# from data import QUESTION_DATA
from quiz_brain import QuizBrain
from ui import QuizInterface

# API
API_ENDPOINT  = "https://opentdb.com/api.php" ##?amount=10&type=boolean"

def main()-> None:
    """ Contains a main loop of a program"""
    question_bank = []

    parameters = {
        "amount":10,
        "type":"boolean"
    }

    response = requests.get(url=API_ENDPOINT,params=parameters,timeout=10)
    response.raise_for_status()
    data = response.json()
    if data['results']:

        for question in data['results']:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)


    quiz = QuizBrain(question_bank)
    QuizInterface(quiz)

    # while quiz.still_has_questions():
    #     quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == '__main__':
    main()
