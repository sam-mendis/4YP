import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello Sam",
                    fg="white",  # Set the text color to white
                    bg="black",
                    width=10,
                    height=10  # Set the background color to black
                    )

button = tk.Button(
    text="New Test",
    width=25,
    height=5,
    bg="black",
    fg="red"
)
label = tk.Label(text="Temp/deg C",
                 fg="white",
                 bg="black"
                 )

entry = tk.Entry(
    fg="yellow",
    bg="blue",
    width=50
)


frame1 = tk.Frame(master=window, width=100, height=100, bg="black")
label1 = tk.Label(master=frame1, text="I'm at (0, 0)", bg="red")
#label1.place(x=0, y=0)
label2 = tk.Label(master=frame1, text="I'm at (75, 75)", bg="yellow")
#label2.place(x=75, y=75)

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        # +1 cos python counts wierdly
        label = tk.Label(master=frame, text=f"Row {i+1}\nColumn {j+1}")
        label.pack()


# greeting.pack()
# button.pack()
# label.pack()
# entry.pack()

#frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


window.mainloop()
