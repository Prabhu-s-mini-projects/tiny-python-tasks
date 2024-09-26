"""main script"""
from quiz_brain import QuizBrain
from question_model import Question
from data import QUESTION_DATA

def main()-> None:
    """Contains on the main"""
    question_bank = []


    for question in QUESTION_DATA:
        question_bank.append(Question(question['text'],question['answer']))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've Completed the quiz")
    print(f"Your score is {quiz.score}/12")

if __name__ == '__main__':
    main()
