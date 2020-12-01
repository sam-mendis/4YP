from tkinter import *

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()


# Creating a function for the button
def myClick():
    mylabel = Label(root, text="Final Temp")
    mylabel.grid(row=1, column=3)


# creating a labels
myLabel1 = Label(root, text="Temperature Controls")
myLabel2 = Label(root, text="Temp/K")

# Creating a button, command calls the function next to command
# remember when using the command button not to but brackets after the function
button_confirm = Button(root, text="Confirm", padx=50, command=myClick)
# using the grid to place pobjects
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=0)
button_confirm.grid(row=1, column=2)


root.mainloop()
