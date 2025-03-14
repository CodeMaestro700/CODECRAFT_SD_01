# File: temperature_converter_gui.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"{temp}°C = {f:.2f}°F, {k:.2f}K")

        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"{temp}°F = {c:.2f}°C, {k:.2f}K")

        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"{temp}K = {c:.2f}°C, {f:.2f}°F")

        else:
            result.set("Please select a valid unit.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create GUI window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("400x250")
window.resizable(False, False)

# Temperature entry
tk.Label(window, text="Enter Temperature:", font=("Arial", 12)).pack(pady=10)
entry_temp = tk.Entry(window, font=("Arial", 12))
entry_temp.pack()

# Unit dropdown
tk.Label(window, text="Select Unit:", font=("Arial", 12)).pack(pady=10)
combo_unit = ttk.Combobox(window, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12), state="readonly")
combo_unit.pack()

# Convert button
tk.Button(window, text="Convert", command=convert_temperature, font=("Arial", 12), bg="lightblue").pack(pady=15)

# Result label
result = tk.StringVar()
tk.Label(window, textvariable=result, font=("Arial", 12), fg="green").pack()

# Start the GUI loop
window.mainloop()
