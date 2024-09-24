# Dependencies
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TITLE_FONT = ("Ariel", 20, "italic")
Score_FONT = ("Ariel", 16, "normal")
RIGHT_PATH = "images/true.png"
WRONG_PATH = "images/false.png"

class QuizInterface:
    """Creates a UI for the Quizzler game"""

    def __init__(self, quiz_brain:QuizBrain):

        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        # Creating a canvas to hold card image
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        # Creating Label
        self.question_text = self.canvas.create_text(150, 100,width=280, text="Some question_text", fill='black', font=TITLE_FONT)


        # Positioning the canvas
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        right_image = PhotoImage(file=RIGHT_PATH)
        wrong_image = PhotoImage(file=WRONG_PATH)

        # Creating right button
        self.right_button = Button(image=right_image, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        # Creating wrong button
        self.wrong_button = Button(image=wrong_image, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        # Creating timer Logo
        self.score_label = Label(text="Score: 0", font=Score_FONT,  bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        self.next_card()

        self.window.mainloop()

    def next_card(self)-> None:
        """Changes to next question"""

        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz_brain.score}")

            q_text = self.quiz_brain.next_question()

            # Changes the value of the item inside a canvas
            self.canvas.itemconfig(self.question_text, text=f"{q_text}", fill="black")
        else:

            self.canvas.itemconfig(self.question_text, text=f"Quiz Completed", fill="black")

            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self)-> None:
        """ Control comes to this method after pressing the right button"""
        self.give_feedback(self.quiz_brain.check_answer("true"))

    def false_pressed(self)-> None:
        """ Control comes to this method after pressing the wrong button"""
        self.give_feedback(self.quiz_brain.check_answer("false"))

    def give_feedback(self,is_right)-> None:
        """based on the is_right updating the canvas color and score"""

        if is_right:
            self.canvas.config(bg="GREEN")
        else:
            self.canvas.config(bg="RED")

        # Waiting for 1000 milli sec
        self.window.after(1000,self.next_card)
