import pandas
from tkinter import *
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def know():
    try:
        to_learn.remove(current_card)
    except ValueError:
        messagebox.showinfo(title="Congrats", message="You Learned all 100 words")
    else:
        data_file = pandas.DataFrame(to_learn)
        data_file.to_csv("./data/words_to_learn.csv", index=False)
        next_card()


def next_card():
    try:
        global current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_background, image=front_image)
        flip_timer = window.after(3000, func=flip_card)
    except ValueError:
        messagebox.showinfo(title="Congrats", message="You Learned all 100 words")
    except IndexError:
        messagebox.showinfo(title="Congrats", message="You Learned all 100 words")


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
canvas.config(highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, 'bold'))
canvas.grid(column=0, columnspan=2, row=0)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=know)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
