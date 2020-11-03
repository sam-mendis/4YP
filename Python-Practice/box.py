import tkinter as tk


def confirm():
    """ if clicked confirm the function will clear screen of other
    parameters and only display inputted parameters with a button labelled confirm
    """
    Temp = entry_temp.get()
    Pressure = entry_pressure.get()
    Gas_A = entry_gas.get()
    input_Temp["text"] = f"{float(Temp)} (\N{DEGREE CELSIUS})"
    input_Pressure["text"] = f"{float(Pressure)} (kPa)"
    input_GasA["text"] = f"{float(Gas_A)} %"


# Creating the window and naming it
window = tk.Tk()
window.title("Model GUI")
window.resizable(width=True, height=True)

# Creating the entry varaibles and buttons
frame_entry = tk.Frame(master=window)
entry_temp = tk.Entry(master=frame_entry, width=10)
label_temp = tk.Label(master=frame_entry, text="Temp (\N{DEGREE CELSIUS})")
entry_pressure = tk.Entry(master=frame_entry, width=10)
label_pressure = tk.Label(master=frame_entry, text="Pressure (kPa)")
entry_gas = tk.Entry(master=frame_entry, width=10)
label_gas = tk.Label(master=frame_entry, text="Gas A %")
label_final = tk.Label(master=frame_entry, text="Final Parameters")

button_next = tk.Button(
    master=frame_entry,
    text="Next",
    command=confirm
)
input_Temp = tk.Label(master=window, text="")
input_Pressure = tk.Label(master=window, text="")
input_GasA = tk.Label(master=window, text="")
button_confirm = tk.Button(
    master=frame_entry,
    text="Confirm"
    # command =some function
)
button_clear = tk.Button(
    master=frame_entry,
    text="Clear"
    # command =some function
)


# Placing the entry variables
frame_entry.grid(row=0, column=0)
label_temp.grid(row=0, column=0)
entry_temp.grid(row=1, column=0)
label_pressure.grid(row=0, column=1)
entry_pressure.grid(row=1, column=1)
label_gas.grid(row=0, column=2)
entry_gas.grid(row=1, column=2)
button_next.grid(row=1, column=3)

label_final.grid(row=6, column=1, sticky="e")
input_Temp.grid(row=3, column=0)
input_Pressure.grid(row=3, column=1)
input_GasA.grid(row=3, column=2)
button_confirm.grid(row=7, column=3)
button_clear.grid(row=5, column=3)
window.mainloop()
