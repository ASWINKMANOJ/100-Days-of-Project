import tkinter

window = tkinter.Tk()

window.title("WINDOW")
window.minsize(width=500, height=300)
label = tkinter.Label(text="I'm a label", font=("Aerial", 23, "normal"))
label.pack(side="right")

window.mainloop()
