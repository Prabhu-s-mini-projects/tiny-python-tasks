# Dependencies
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TITLE_FONT = ("Ariel", 20, "italic")
Score_FONT = ("Ariel", 16, "normal")
RIGHT_PATH = "images/true.png"
WRONG_PATH = "images/false.png"

class QuizInterface:

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
        right_button = Button(image=right_image, command=self.next_card)
        right_button.grid(row=2, column=0)

        # Creating wrong button
        wrong_button = Button(image=wrong_image, command=self.flip_card)
        wrong_button.grid(row=2, column=1)

        # Creating timer Logo
        score_label = Label(text="Score: 0", font=Score_FONT,  bg=THEME_COLOR, highlightthickness=0)
        score_label.grid(row=0, column=1)

        self.next_card()

        self.window.mainloop()

    def next_card(self)-> None:
        q_text = self.quiz_brain.current_question
        # Changes the value of the item inside a canvas
        self.canvas.itemconfig(self.question_text, text=f"{q_text}", fill="black")

    def flip_card(self)-> None:
        print("wrong")
