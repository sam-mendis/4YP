from tkinter import *

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()
# creating a labels
myLabel1 = Label(root, text="Temperature Controls")
myLabel2 = Label(root, text="Temp/K")
# using the grid
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=0)

root.mainloop()
