from tkinter import *

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()
# Naming the Gui
root.title("Environmental Controller for Test Cell")
# Making an icon
# root.iconbitmap('control.png')
frame_s = Frame(root)
frame_s.grid()


# Creating the input table
inputlabel = Label(frame_s, text="Manual Input", font=" Times 16", width=35)
inputlabel.grid(row=0, column=0, columnspan=6)
templabel = Label(
    frame_s, text="Temp/\N{DEGREE SIGN}C", font=" Times 14", width=7)
templabel.grid(row=2, column=0)


timelabel = Label(frame_s, text="Time", bd=1, relief="solid",
                  font=" Times 14", width=26)
timelabel.grid(row=1, column=1, columnspan=3)
timelabeldays = Label(frame_s, text="Days", font=" Times 14", width=7)
timelabeldays.grid(row=2, column=1)
timelabelhours = Label(frame_s, text="Hours", font=" Times 14", width=7)
timelabelhours.grid(row=2, column=2)
timelabelmins = Label(frame_s, text="Minutes", font=" Times 14", width=7)
timelabelmins.grid(row=2, column=3)

gas1label = Label(frame_s, text="Gas A %", font=" Times 14", width=7)
gas1label.grid(row=2, column=4,)
gas2label = Label(frame_s, text="Gas B %", font=" Times 14", width=7)
gas2label.grid(row=2, column=5)

e_temp = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_temp.grid(row=3, column=0)

e_timed = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_timed.grid(row=3, column=1)
e_timeh = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_timeh.grid(row=3, column=2)
e_timem = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_timem.grid(row=3, column=3)

e_gas1 = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_gas1.grid(row=3, column=4)
e_gas2 = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_gas2.grid(row=3, column=5)

# Creating a button, command calls the function next to command
# remember when using the command button not to but brackets after the function
button_next = Button(frame_s, text="Next", command=next)
button_next.grid(row=3, column=6)

# Creating entries to input data
#e_t = Entry(root, width=50, borderwidth=5)
# e   _t.grid(row=15, column=0, columnspan=3, padx=10, pady=10)
# labeling the entry field
# e_t.insert(
# 0, "Enter Desired Temperature, between 25\N{DEGREE SIGN}C and 120\N{DEGREE SIGN}C")
# Creating a function for the button

# making sure you are collecting the entry using e.get


def next():
    global temp_i, timed_i, timeh_i, timem_i
    temp_i = e_temp.get()
    timed_i = e_timed.get()
    timeh_i = e_timeh.get()
    timem_i = e_timem.get()
    frame_n = Frame(root)
    frame_n.grid()
    templ = Label(frame_n, text="Temperature for test")
    timel = Label(frame_n, text="Time for test")
    gasl = Label(frame_n, text="Gas % s")
    tempinput = "Steady State Temp = " + temp_i + "\N{DEGREE SIGN}C"
    timeinput = timed_i + "Days " + timeh_i +\
        "H " + timem_i + "min"
    f_templabel = Label(frame_n, text=tempinput)
    f_timelabel = Label(frame_n, text=timeinput)
    frame_s.destroy()
    templ.grid(row=1, column=1)
    timel.grid(row=1, column=2)
    gasl.grid(row=1, column=3)
    f_templabel.grid(row=2, column=1)
    f_timelabel.grid(row=2, column=2)


# creating a labels


root.mainloop()
