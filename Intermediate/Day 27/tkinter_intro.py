import tkinter

window = tkinter.Tk()

window.title("WINDOW")
window.minsize(width=500, height=300)
label = tkinter.Label(text="I'm a label", font=("Aerial", 23, "normal"))
label.pack(side="top")


def buttonClicked():
    global label
    label.config(text=input.get())


label["text"] = "New Text"
label.config(text="New Text")
button = tkinter.Button(text="Click ME", command=buttonClicked)
button.pack()

input = tkinter.Entry()
input.pack()


window.mainloop()
