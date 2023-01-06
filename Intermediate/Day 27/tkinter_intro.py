import tkinter

window = tkinter.Tk()

window.title("WINDOW")
window.minsize(width=500, height=300)
window.config(padx=30, pady=20)
label = tkinter.Label(text="I'm a label", font=("Aerial", 23, "normal"))
label.grid(column=0, row=0)


def buttonClicked():
    global label
    label.config(text=input.get())


label["text"] = "New Text"
label.config(text="New Text")
button = tkinter.Button(text="Click ME", command=buttonClicked)
button.grid(column=1, row=1)
button2 = tkinter.Button(text="another button")
button2.grid(column=2, row=0)
input = tkinter.Entry(width=50)
input.grid(column=3, row=2)

window.mainloop()
