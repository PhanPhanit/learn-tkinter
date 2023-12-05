from tkinter import *




root = Tk()



e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name here.")

def button_click():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Click Me", padx=8, command=button_click)
myButton.pack()


root.mainloop()