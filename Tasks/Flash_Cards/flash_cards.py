""" Contains the main UI file for Flash card Game for KIDS """

# Dependencies
import random
from tkinter import Tk, Canvas, Button, PhotoImage

import pandas

# Internal modules
# TBD

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_PATH  = "Database/card_back.png"
CARD_FRONT_PATH = "Database/card_front.png"
RIGHT_PATH = "Database/right.png"
WRONG_PATH = "Database/wrong.png"
TITLE_FONT = ("Ariel", 40, "italic")
MESSAGE_FONT = ("Ariel", 60, "bold")

# Global Variables
CURRENT_CARD = {'English': 'English', 'French': 'French'}
FLIP_TIMER = {'English': 'English', 'French': 'French'}

def main()-> None:
    """ The Flash card contains english and French words """


    # ---------------------------- loading data from csv ------------------------------- #
    try:
        words_dataframe = pandas.read_csv("Database/words_to_learn.csv")
    except FileNotFoundError:
        words_dataframe = pandas.read_csv("Database/french_words.csv")

    #mapping_of_words = { row.French: row.English for index, row in words_dataFrame.iterrows()}

    dictionary_of_words = words_dataframe.to_dict(orient="records")

    print(dictionary_of_words)

    # ---------------------------- UI  ------------------------------- #

    # Creating a screen
    window = Tk()
    window.title("Flash Card game")
    window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

    # Loading the cards' image
    card_back_image = PhotoImage(file=CARD_BACK_PATH)
    card_front_image = PhotoImage(file=CARD_FRONT_PATH)
    right_image = PhotoImage(file=RIGHT_PATH)
    wrong_image = PhotoImage(file=WRONG_PATH)

    # Creating a canvas to hold card image
    canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

    # Appending image to the canvas
    bg_image = canvas.create_image(400,268, image=card_front_image)

    # Creating Label
    tittle_text = canvas.create_text(400, 130, text ="Title", fill='black',font=TITLE_FONT)
    message_text = canvas.create_text(400, 268, text ="Message", fill='black', font=MESSAGE_FONT)

    # Positioning the canvas
    canvas.grid(row=0,column=0,columnspan=2)

    # ---------------------------- Functionality  ------------------------------- #

    def next_card()-> None:
        """ fetches the next card"""

        #pick a random card
        global CURRENT_CARD

        # cancel and restart the timer
        # window.after_cancel(FLIP_TIMER)

        if CURRENT_CARD:
            # global current_card
            # remove the current word
            dictionary_of_words.remove(CURRENT_CARD)

            # save it to the new file
            # updated_dict = {"French":"English"}
            # updated_dict.update({item.get("French"):item.get("English")
            # for item in dictionary_of_words})

            # Updated dataframe
            updated_dataframe = pandas.DataFrame.from_records(dictionary_of_words)
            updated_dataframe.to_csv("Database/words_to_learn.csv", index=False)

        # fetching the random card
        global CURRENT_CARD
        CURRENT_CARD = random.choice(dictionary_of_words)
        french_word = CURRENT_CARD.get("French")

        # Changes the value of the item inside a canvas
        canvas.itemconfig(tittle_text, text="French", fill="black")
        canvas.itemconfig(message_text, text=french_word, fill="black")
        canvas.itemconfig(bg_image, image=card_front_image)

        # starting the timer
        #FLIP_TIMER = window.after(3000, func=flip_card)


    def flip_card()-> None:
        """flips the card back and share the respective word"""
        #global CURRENT_CARD

        canvas.itemconfig(tittle_text,text="English", fill="white")
        #canvas.itemconfig(message_text, text=CURRENT_CARD.get("English"), fill="white")
        canvas.itemconfig(bg_image, image=card_back_image)


    # Creating right button
    right_button = Button(image=right_image,
                          command=next_card, highlightbackground=BACKGROUND_COLOR)
    right_button.grid(row=2,column=1)

    # Creating wrong button
    wrong_button = Button(image=wrong_image,
                          command=flip_card, highlightbackground=BACKGROUND_COLOR)
    wrong_button.grid(row=2,column=0)

    #global FLIP_TIMER
    #FLIP_TIMER = window.after(3000, func=flip_card)
    next_card()


    window.mainloop()

if __name__ == '__main__':
    main()
