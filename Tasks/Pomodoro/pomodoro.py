""" Main script of program"""
import math
from tkinter import Tk, Label,Button,PhotoImage,Canvas

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def on_click_reset()-> None:
    """Resets the clock"""
    print("yet to code")

# ---------------------------- UI SETUP ------------------------------- #
def main()-> None:
    """start of program"""

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def on_click_start() -> None:
        """Start the timer"""
        text = ""
        for _ in range(4):
            count_down(WORK_MIN * 60)
            count_down(SHORT_BREAK_MIN if _ != 3 else LONG_BREAK_MIN * 60)
            text += "✔"
            check_label.config(text=text)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def count_down(count: int) -> None:
        """ To track the countdown flow"""
        mint = math.floor(count / 60)
        sec = math.floor(count % 60)

        # To change value of a item inside a canvas
        canvas.itemconfig(timer_text, text=f"{mint}:{sec}")
        if count > 0:
            # Using instead of while loop.
            window.after(1000, count_down, count - 1)
    window = Tk()
    window.title("POMODORO Timer")
    window.config(padx=100,pady=50,bg=YELLOW)

    # Creating timer Logo
    timer_label = Label(text="Timer",
                        fg=GREEN,
                        font=(FONT_NAME, "40", "bold"),
                        bg=YELLOW, highlightthickness=0)
    timer_label.grid(row=0,column=1)

    # creating an Image and label with timer count down
    canvas = Canvas(width =206, height =224,bg=YELLOW,highlightthickness=0)
    tomato_image = PhotoImage(file= "tomato.png")
    canvas.create_image(103,112,image=tomato_image)
    timer_text = canvas.create_text(103,130,text ="00:00",
                                    fill="white", font=(FONT_NAME,"24","bold"))
    canvas.grid(row=1,column=1)

    # creating start button
    start_button = Button(text="Start", highlightbackground=YELLOW, command=on_click_start)
    start_button.grid(row=2,column=0)

    # creating Reset button
    start_button = Button(text="Reset", highlightbackground=YELLOW, command=on_click_reset)
    start_button.grid(row=2,column=2)

    # creating Check mark label
    check_label = Label(text="✔", fg=GREEN,bg=YELLOW, highlightthickness= 0)
    check_label.grid(row=3,column=1)

    window.mainloop()

if __name__ =='__main__':
    main()
