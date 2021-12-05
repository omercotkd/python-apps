import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
from string import ascii_letters
import pyperclip

font = ("Ariel", 10, "bold")
DEFAULT_USERNAME = "omercotkd@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ascii_letters
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # get the data from the user input
    website = website_entry.get().lower()
    user = user_name_entry.get()
    password = password_entry.get()

    # check if the user entered any data and if not popup a warning message
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
        is_ok = False
    else:
        # asks the user if the details entered are ok
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {user}\n"
                                                              f"Password: {password}\n")
        # save the data to a file
        if is_ok:
            with open("saved_passwords.txt", "a") as f:
                f.write(f"{website}|{user}|{password}\n")
            # del the data in the entry boxes
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            website_entry.focus()
        else:
            pass


# ---------------------------- GET SAVED PASSWORD AND USER NAME ------------------------------- #


def get_info():
    exists = False
    website = website_entry.get().lower()
    # checks if the website entered is a valid one
    if len(website) > 0:
        # get the saved users file
        with open("saved_passwords.txt", "r") as f:
            info = f.readlines()

        # checks if there is a user for that website and if so show the user for the user
        for i in info:
            if i.startswith(website):
                (website, user_name, password) = i.split("|")
                messagebox.showinfo(title=f"{website.capitalize()} user info:", message=f"User name: {user_name}\n"
                                                                                         f"Password: {password}")
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                website_entry.focus()
                exists = True

    # if couldn't find the website shows this massage
    if not exists:
        messagebox.showinfo(title="Oops", message=f"Couldn't find User name and Password for this website: {website}")


# ---------------------------- UI SETUP ------------------------------- #
# screen setup
screen = tk.Tk()
screen.config(padx=40, pady=50)
screen.title("Password Manager")

# logo setup
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# labels setup
website_label = tk.Label(text="Website:", font=font)
website_label.grid(row=1, column=0, sticky="W")
user_name_label = tk.Label(text="Email/Username:", font=font)
user_name_label.grid(row=2, column=0, sticky="W")
password_label = tk.Label(text="Password:", font=font)
password_label.grid(row=3, column=0, sticky="W")

# entry boxes setup
website_entry = tk.Entry(width=51, font=font)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()
user_name_entry = tk.Entry(width=51, font=font)
user_name_entry.grid(row=2, column=1, columnspan=2, sticky="W")
user_name_entry.insert(0, DEFAULT_USERNAME)
password_entry = tk.Entry(width=32, font=font)
password_entry.grid(row=3, column=1, sticky="W")

# buttons setup
generate_pass_button = tk.Button(text="Generate Password", font=font, highlightthickness=0, command=generate_password)
generate_pass_button.grid(row=3, column=2, sticky="W")
add_button = tk.Button(text="Add", width=44, font=font, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")
get_button = tk.Button(text="Get Password", width=44, font=font,command=get_info)
get_button.grid(row=5, column=1, columnspan=2, sticky="W")

screen.mainloop()
