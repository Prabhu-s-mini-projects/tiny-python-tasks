# Dependencies
from tkinter import *
from tkinter import messagebox # message box is not a class. So we need to import  separately.
import pyperclip

# Internal modules
from Controller.password_generator import PasswordManager


# CONSTANTS
LOGO_PATH = "Database/logo.png"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password()-> None:

    # Generate a password
    password_manager = PasswordManager()
    password = password_manager.generate()

    # Updating the password
    entered_password.insert(0,password)

    # Storing the password in clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save()-> None:

    password =  entered_password.get()
    website = entered_website.get()
    email = entered_email.get()

    # will all user to save data only after all the details are entered
    if email and password and website:

        # Display a pop-up message box with entered credentials
        is_ok = messagebox.askokcancel( title= website ,message=f"Here are entered Credentials\n "
                                                              f"Email:{email} \n "
                                                              f"password:{password} \n"
                                                              f" Please confirm to save ")

        if is_ok:

            # Save the data to the file
            with open("passwords.txt","a") as file:
                file.writelines(f"{website}| {email} | {password}\n")

            # Deletes the data in the text box.
            entered_website.delete(0,END)
            entered_password.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

# Creating a window
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# Creating a canvas to display a logo
canvas = Canvas(width =200, height =200)
logo = PhotoImage(file=LOGO_PATH)
canvas.create_image(100,100,image= logo)
canvas.grid(row=0, column=1)

# Creating a website label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

# Creating a username_email_label
email_label = Label(text="Email/UserName:")
email_label.grid(row=2,column=0)

# Creating a website label
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# Creating input textbox for website
entered_website = Entry(width=38)
entered_website.grid(row=1,column=1, columnspan=2)

# To keep the cursor in the textbox
entered_website.focus()

# Creating input textbox for email/username
entered_email = Entry(width=38)
entered_email.grid(row=2,column=1, columnspan=2)

# Having an email
entered_email.insert(0,"prabhu@gmail.com")

# Creating input textbox for password
entered_password = Entry(width=21)
entered_password.grid(row=3, column=1)

# Creating a generate Button
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

# Creating an add button
add = Button(text="add",width=36,command=save)
add.grid(row=4,column=1,columnspan=2)

#Keep the program running
window.mainloop()
