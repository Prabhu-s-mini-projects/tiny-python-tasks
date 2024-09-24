""" Script that converts miles to KM """
# Dependencies
from tkinter import Tk,Entry,Label,Button

def main()-> None:
    """Contains the main loop of a program"""

    window = Tk()
    window.title("Conversion Tittle")
    window.config(padx=10, pady=10)

    def on_mile_kilometer_click() -> None:
        """ perform conversion calculations"""
        entered_miles = float(miles.get())
        calculated_km = round(entered_miles * 1.609344)
        km.config(text=f"{calculated_km}")

    def on_f_to_c_click() -> None:
        """Performs Fahrenheit to Celsius calculations"""
        entered_f = float(fahrenheit.get())
        calculated_c = round((entered_f - 32) * 5 / 9)
        celsius.config(text=f"{calculated_c}")

    # Creating a Mile to KM
    miles = Entry(width=5)
    miles.grid(row =1, column = 1)

    miles_label = Label(text="miles")
    miles_label.grid(row =1, column = 2)

    convert_m_2_k = Button(text="convert", command=on_mile_kilometer_click)
    convert_m_2_k.grid(row=1,column=3)

    equal_label = Label(text="is equal to")
    equal_label.grid(row=1,column=4)

    km = Label(text="",width=5)
    km.grid(row=1,column=5)

    km_label = Label(text="Km")
    km_label.grid(row=1,column=6)

    # F to C
    fahrenheit = Entry(width=5)
    fahrenheit.grid(row =2, column = 1)

    fahrenheit_label = Label(text="'F")
    fahrenheit_label.grid(row =2, column = 2)

    convert_f_2_c = Button(text="convert", command=on_f_to_c_click)
    convert_f_2_c.grid(row=2,column=3)

    eq_label = Label(text="is equal to")
    eq_label.grid(row=2,column=4)

    celsius = Label(text="",width=5)
    celsius.grid(row=2,column=5)

    celsius_label = Label(text="'C")
    celsius_label.grid(row=2,column=6)


    window.mainloop()

if __name__ == '__main__':
    main()