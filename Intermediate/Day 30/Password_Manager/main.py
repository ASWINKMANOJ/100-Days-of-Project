from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 3)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password = password_letters + password_numbers + password_symbols

    random.shuffle(password)
    new_pas = ""
    for char in password:
        new_pas += char
    pyperclip.copy(new_pas)
    password_entry.delete(0, END)
    password_entry.insert(0, new_pas)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {website: {"email": email,
                          "password": password}}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        val = messagebox.showinfo("Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)

        else:
            data.update(new_dict)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website_entered = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            file = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website_entered in file:
            email = file[website_entered]["email"]
            password = file[website_entered]["password"]
            messagebox.showinfo(title=website_entered, message=f"Email : {email} \nPassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website_entered} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Courier", 10, "normal"), bg="white")
website_label.grid(column=0, row=1, pady=5)
website_entry = Entry(width=60)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="nesw", pady=5)
search_button = Button(text="Search", font=("Courier", 10, "normal"), command=search)
search_button.grid(column=2, row=1, sticky="nesw", pady=5)

email_label = Label(text="Email/Username:", font=("Courier", 10, "normal"), bg="white")
email_label.grid(column=0, row=2, pady=10)
email_entry = Entry()
email_entry.insert(0, "aswinachoozzzakm@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="nesw", pady=5)

password_label = Label(text="Password:", font=("Courier", 10, "normal"), bg="white")
password_label.grid(column=0, row=3, pady=5)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="nesw", pady=5)
generate_button = Button(text="Generate Password", font=("Courier", 10, "normal"), command=generate)
generate_button.grid(column=2, row=3, sticky="nesw", pady=5)

add_button = Button(text="Add", font=("Courier", 10, "normal"), command=save_password)
add_button.grid(column=1, columnspan=2, row=4, sticky="nesw", pady=5)

window.mainloop()
