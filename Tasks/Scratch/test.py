from  tkinter import *

def on_button_clicked()-> None:
    print("button clicked")
    # label["text"] = "Button Clicked"  # this one and line below both does the same thing.
    # But the bottom code is more read able and relevant.
    # Label.config("text = Button clicked")
    entered_text = input_text.get()
    label.config(text=entered_text)

# Creating a window
window = Tk()
window.title("First GUI program")
window.minsize(width=500,height=500)

# there are 3 layout
# pack:  Just pack the data one on another
# place: place the item at x and y position
# grid: place them in call that contains rows and column

# creating a label
label = Label(text=" I am a label", font=("Ariel", "24", "bold"))
# packer is need to show it as part of a window
#label.pack()
label.grid(row=0, column=0)

# input text box
input_text = Entry()
#input_text.pack()
input_text.grid(row=2,column=3)

# creating a Button
button  = Button(text="click Me!", command=on_button_clicked)
#button.pack()
button.grid(row=1,column=1)

new_button = Button(text="new_click Me!", command=on_button_clicked)
new_button.grid(row=0,column=2)

# will keep the window running
window.mainloop()



def add(*args)->int:
    total = 0
    for arg in args:
        total += arg
    return total

result = add(1,2,3,4,5,6,7,8,9,10)

print(result)

def calculate(n,**kwargs)-> int:
    n += kwargs["add"]
    n *= kwargs["mul"]
    return n

result = calculate(5, add=5,mul=6)

print(result)