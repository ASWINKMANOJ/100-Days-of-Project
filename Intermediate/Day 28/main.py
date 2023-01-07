import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
marks = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    reset_mark = ''
    label_check.config(text=reset_mark)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="BREAK", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW, highlightthickness=0)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="BREAK", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW, highlightthickness=0)
    else:
        count_down(work_sec)
        label_timer.config(text="WORK", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        global marks
        start_timer()
        marks = ""
        for i in range(math.floor(reps / 2)):
            marks += "✓"
        label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
im = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=im)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

label_timer = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label_timer.grid(column=1, row=0)
label_check = tk.Label(highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label_check.grid(column=1, row=3)
start = tk.Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
reset = tk.Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)
window.mainloop()
