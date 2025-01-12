# ui/gui.py
import tkinter as tk
from tkinter import messagebox
from utils.bmi_calculator import calculate_bmi, get_bmi_category
from utils.validation import validate_input
from data.storage import add_user_data, load_data
from data.visualization import plot_user_data
from datetime import datetime
from data.visualization import plot_user_data


def on_calculate():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Invalid Input", "Please enter a valid name.")
        return

    weight = validate_input(weight_entry.get(), 10, 500)
    height = validate_input(height_entry.get(), 0.5, 2.5)

    if weight is None or height is None:
        messagebox.showerror("Invalid Input", "Please enter valid weight and height.")
        return

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    result_label.config(text=f"BMI: {bmi} ({category})")

    # Save Data for the user
    add_user_data(name, weight, height, bmi)


def on_view_trends():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Invalid Input", "Please enter a valid name to view trends.")
        return

    user_data = load_data()
    plot_user_data(user_data, name)


# Main GUI
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")

tk.Label(root, text="Enter Your Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_btn = tk.Button(root, text="Calculate", command=on_calculate)
calculate_btn.pack()

result_label = tk.Label(root, text="")
result_label.pack()

view_trends_btn = tk.Button(root, text="View Your BMI Trends", command=on_view_trends)
view_trends_btn.pack()

root.mainloop()
