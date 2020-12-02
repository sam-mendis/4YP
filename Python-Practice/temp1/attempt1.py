from tkinter import *

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()
# Naming the Gui
root.title("Environmental Controller for Test Cell")
# Creating the input table
inputlabel = Label(root, text="Manual Input")
inputlabel.grid(row=0, column=0, columnspan=6)
templabel = Label(root, text="Temp/\N{DEGREE SIGN}C")
templabel.grid(row=1, column=0, rowspan=2)


timelabel = Label(root, text="Time")
timelabel.grid(row=1, column=1, columnspan=3)
timelabeldays = Label(root, text="Days")
timelabeldays.grid(row=2, column=1)
timelabelhours = Label(root, text="Hours")
timelabelhours.grid(row=2, column=2)
timelabelmins = Label(root, text="Minutes")
timelabelmins.grid(row=2, column=3)

gas1label = Label(root, text="Gas A %")
gas1label.grid(row=1, column=4, rowspan=2)
gas2label = Label(root, text="Gas B %")
gas2label.grid(row=1, column=5, rowspan=2)

e_temp = Entry(root)
e_temp.grid(row=3, column=0)

e_timed = Entry(root)
e_timed.grid(row=3, column=1)
e_timeh = Entry(root)
e_timeh.grid(row=3, column=2)
e_timem = Entry(root)
e_timem.grid(row=3, column=3)

e_gas1 = Entry(root)
e_gas1.grid(row=3, column=4)


# Creating entries to input data
e_t = Entry(root, width=50, borderwidth=5)
e_t.grid(row=15, column=0, columnspan=3, padx=10, pady=10)
# labeling the entry field
e_t.insert(
    0, "Enter Desired Temperature, between 25\N{DEGREE SIGN}C and 120\N{DEGREE SIGN}C")
# Creating a function for the button


def myClick():
    # making sure you are collecting the entry using e.get
    tempinput = "Final Temp = " + e.get() + "K"
    mylabel = Label(root, text=tempinput)
    mylabel.grid(row=15, column=3)


# creating a labels
myLabel1 = Label(root, text="Temperature Controls")
myLabel2 = Label(root, text="Temp/K")

# Creating a button, command calls the function next to command
# remember when using the command button not to but brackets after the function
button_confirm = Button(root, text="Confirm", padx=5, command=myClick)


# using the grid to place pobjects
myLabel1.grid(row=16, column=1)
myLabel2.grid(row=16, column=0)
button_confirm.grid(row=6, column=2)


root.mainloop()
