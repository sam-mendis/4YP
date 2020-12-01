from tkinter import *

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()
# creating a labels
myLabel1 = Label(root, text="Temperature Controls")
myLabel2 = Label(root, text="Temp/K")

# Creating a button
button_confirm = Button(root, text="Confirm", padx=50, pady=50)
# using the grid to place pobjects
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=0)
button_confirm.grid(row=1, column=2)


root.mainloop()
