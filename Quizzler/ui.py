# Dependencies
from tkinter import *

THEME_COLOR = "#375362"
TITLE_FONT = ("Ariel", 20, "italic")
Score_FONT = ("Ariel", 16, "normal")
RIGHT_PATH = "images/true.png"
WRONG_PATH = "images/false.png"

class QuizInterface:

    def __init__(self):


        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        # Creating a canvas to hold card image
        canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        # Creating Label
        tittle_text = canvas.create_text(150, 100, text="Title", fill='black', font=TITLE_FONT)

        # Changes the value of the item inside a canvas
        canvas.itemconfig(tittle_text, text="French", fill="black")

        # Positioning the canvas
        canvas.grid(row=1, column=0, columnspan=2,pady=50)

        right_image = PhotoImage(file=RIGHT_PATH)
        wrong_image = PhotoImage(file=WRONG_PATH)

        # Creating right button
        right_button = Button(image=right_image)#, command=self.next_card)
        right_button.grid(row=2, column=0)

        # Creating wrong button
        wrong_button = Button(image=wrong_image)#, command=self.flip_card)
        wrong_button.grid(row=2, column=1)

        # Creating timer Logo
        score_label = Label(text="Score: 0", font=Score_FONT,  bg=THEME_COLOR, highlightthickness=0)
        score_label.grid(row=0, column=1)


        self.window.mainloop()

        def next_card()-> None:
            print("right")

        def flip_card()-> None:
            print("wrong")
