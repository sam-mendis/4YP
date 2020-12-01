from tkinter import *

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()
# creating a label widget
myLabel = Label(root, text="Hello World")
# shoving the label onto the screen
myLabel.pack()

root.mainloop()
