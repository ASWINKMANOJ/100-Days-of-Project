import tkinter as tk

window = tk.Tk()

window.title("Mile to Km Converter")
window.minsize(width=400, height=250)
window.config(pady=30, padx=40)
km = 0


def converter():
    global km
    miles = int(entry.get())
    km = round((miles * 1.6), 3)
    label4.config(text=km, font=("Aerial", 23, "normal"))


label1 = tk.Label(text="Miles", font=("Aerial", 23, "normal"))
label1.grid(column=2, row=0)

entry = tk.Entry()
entry.grid(column=1, row=0)

label2 = tk.Label(text="Km", font=("Aerial", 23, "normal"))
label2.grid(column=2, row=1)

label3 = tk.Label(text="is equal to", font=("Aerial", 23, "normal"))
label3.grid(column=0, row=1)

label4 = tk.Label(text=km, font=("Aerial", 23, "normal"))
label4.grid(column=1, row=1)

button = tk.Button(text="Calculate", font=("Aerial", 23, "normal"), command=converter)
button.grid(column=1, row=2)

window.mainloop()
