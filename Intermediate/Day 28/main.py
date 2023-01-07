import tkinter as tk

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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
im = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=im)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

label_timer = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label_timer.grid(column=1, row=0)
label_check = tk.Label(text="✔", highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label_check.grid(column=1, row=3)
start = tk.Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0)
reset = tk.Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)
window.mainloop()
