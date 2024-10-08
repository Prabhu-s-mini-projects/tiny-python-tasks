""" Main script"""
# Dependencies
import json
from tkinter import Tk, Label, Canvas, PhotoImage, Entry, Button
from tkinter import messagebox, END  # message box is not a class.

# So we need to import separately.
import pyperclip

# Internal modules
from Controller.password_generator import PasswordGenerator

# CONSTANTS
LOGO_PATH = "Database/logo.png"


# ---------------------------- UI SETUP ------------------------------- #

def main()-> None:
    """Start of a program"""

    # ---------------------------- Search  ------------------------------- #
    def search() -> None:
        """search for the entire password in the JSON"""

        # Fetch the website name
        website = entered_website.get()

        try:  # For the first time JSON file is not available or deleted

            # reading the stored Passwords
            with open("passwords.json", 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

        except FileNotFoundError:
            messagebox.showinfo(title="NOT FOUND",
                                message="Entered Website is not in database\n")

        else:

            if website.lower() in data.keys():
                credentials = data.get(website.lower())
                messagebox.showinfo(title=website,
                                    message="Here are the Credentials\n"
                                           f"Email : {credentials.get('email')}\n"
                                           f"password: {credentials.get('password')}")
            else:
                messagebox.showinfo(title="NOT FOUND",
                                    message="Entered Website is not in database\n")

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_password() -> None:
        """generates password"""

        # Generate a password
        password_generator = PasswordGenerator()
        password = password_generator.generate()

        # Updating the password
        entered_password.insert(0, password)

        # Storing the password in clipboard
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def save() -> None:
        """save the password to JSON file"""

        # Fetching the data from the list
        password = entered_password.get()
        website = entered_website.get()
        email = entered_email.get()

        # Creating new entry in the form dict
        new_data = {
            website.lower(): {
                "email": email,
                "password": password
            }
        }

        # will all user to save data only after all the details are entered
        if email and password and website:

            # Display a pop-up message box with entered credentials
            is_ok = messagebox.askokcancel(title=website, message=f"Here are entered Credentials\n "
                                                                  f"Email:{email} \n "
                                                                  f"password:{password} \n"
                                                                  f" Please confirm to save ")

            if is_ok:

                # Save the data to text file
                with open("passwords.txt", "a", encoding="utf-8") as file:
                    file.writelines(f"{website}| {email} | {password}\n")

                try:
                    with open("passwords.json", 'r', encoding="utf-8") as json_file:
                        data = json.load(json_file)

                except FileNotFoundError:
                    with open("passwords.json", "w", encoding="utf-8") as file:
                        json.dump(file, new_data, indent=4)
                else:

                    # updating the data
                    data.update(new_data)

                    # writing the data
                    with open("passwords.json", 'w', encoding="utf-8") as json_file:
                        json.dump(json_file, data, indent=4)

                # Deletes the data in the text box.
                entered_website.delete(0, END)
                entered_password.delete(0, END)

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
    entered_website = Entry(width=21)
    entered_website.grid(row=1,column=1)

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

    # Creating a search Button
    search_button = Button(text="Search",command=search,width=13)
    search_button.grid(row=1,column=2)

    # Creating a generate Button
    generate_button = Button(text="Generate Password",command=generate_password)
    generate_button.grid(row=3,column=2)

    # Creating add button
    add = Button(text="add",width=36,command=save)
    add.grid(row=4,column=1,columnspan=2)

    #Keep the program running
    window.mainloop()

if __name__ == '__main__':
    main()
