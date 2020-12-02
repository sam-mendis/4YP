from tkinter import *

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()
frame_s = Frame(root)
frame_s.grid()

frame_n = Frame(root)
frame_n.grid()
# Naming the Gui
root.title("Environmental Controller for Test Cell")
# Creating the input table
inputlabel = Label(frame_s, text="Manual Input", bd=1,
                   relief="solid", font=" Times 16")
inputlabel.grid(row=0, column=0, columnspan=6)
templabel = Label(
    frame_s, text="Temp/\N{DEGREE SIGN}C", bd=1, relief="solid", font=" Times 14", width=7)
templabel.grid(row=1, column=0, rowspan=2)


timelabel = Label(frame_s, text="Time", bd=1, relief="solid",
                  font=" Times 14", width=7)
timelabel.grid(row=1, column=1, columnspan=3)
timelabeldays = Label(frame_s, text="Days", bd=1,
                      relief="solid", font=" Times 12", width=7)
timelabeldays.grid(row=2, column=1)
timelabelhours = Label(frame_s, text="Hours", bd=1,
                       relief="solid", font=" Times 12", width=7)
timelabelhours.grid(row=2, column=2)
timelabelmins = Label(frame_s, text="Minutes", bd=1,
                      relief="solid", font=" Times 12", width=7)
timelabelmins.grid(row=2, column=3)

gas1label = Label(frame_s, text="Gas A %", bd=1,
                  relief="solid", font=" Times 14", width=7)
gas1label.grid(row=1, column=4, rowspan=2)
gas2label = Label(frame_s, text="Gas B %", bd=1,
                  relief="solid", font=" Times 14", width=7)
gas2label.grid(row=1, column=5, rowspan=2)

e_temp = Entry(frame_s, bd=1, relief="solid", width=7)
e_temp.grid(row=3, column=0)

e_timed = Entry(frame_s, width=7)
e_timed.grid(row=3, column=1)
e_timeh = Entry(frame_s, width=7)
e_timeh.grid(row=3, column=2)
e_timem = Entry(frame_s, width=7)
e_timem.grid(row=3, column=3)

e_gas1 = Entry(frame_s, width=7)
e_gas1.grid(row=3, column=4)
e_gas2 = Entry(frame_s, width=7)
e_gas2.grid(row=3, column=5)


# Creating entries to input data
#e_t = Entry(root, width=50, borderwidth=5)
# e   _t.grid(row=15, column=0, columnspan=3, padx=10, pady=10)
# labeling the entry field
# e_t.insert(
# 0, "Enter Desired Temperature, between 25\N{DEGREE SIGN}C and 120\N{DEGREE SIGN}C")
# Creating a function for the button


def next():
    # making sure you are collecting the entry using e.get
    frame_s.destroy()
    tempinput = "Steady State Temp = " + e_temp.get() + "\N{DEGREE SIGN}C"
    timeinput = e_timed.get() + "Days " + e_timeh.get() + \
        "h " + e_timem.get() + "min"
    f_templabel = Label(frame_n, text=tempinput)
    f_timelabel = Label(frame_n, text=timeinput)

    f_templabel.grid(row=1, column=1)


# creating a labels
# Creating a button, command calls the function next to command
# remember when using the command button not to but brackets after the function
button_confirm = Button(frame_s, text="Confirm", command=next)


# using the grid to place pobjects
button_confirm.grid(row=2, column=6, rowspan=2)


root.mainloop()
