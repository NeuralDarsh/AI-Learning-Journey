# Introducing Tkinter for Graphical User Interfaces (GUI)

import tkinter

def calculate_miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=f"{km}")

# 1. Create the window
window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# 2. Input Field
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

# 3. Labels
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

# 4. Button
calculate_button = tkinter.Button(text="Calculate", command=calculate_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()