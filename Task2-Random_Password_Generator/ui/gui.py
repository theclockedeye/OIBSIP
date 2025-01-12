# ui/gui.py
import tkinter as tk
from tkinter import messagebox
from utils.password_generator import generate_password, copy_to_clipboard
from data.password_rules import validate_length

def on_generate():
    try:
        length = int(entry_length.get())
        use_uppercase = var_uppercase.get()
        use_lowercase = var_lowercase.get()
        use_digits = var_digits.get()
        use_symbols = var_symbols.get()

        # Validate length
        validate_length(length)

        # Generate password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)

        # Display the password
        label_result.config(text=password)

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def on_copy():
    password = label_result.cget("text")
    if password:
        copy_to_clipboard(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# Create the main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("300x300")  # Set window size

# Center the window
root.eval('tk::PlaceWindow %s center' % str(root.winfo_toplevel()))

# Create a frame for centering
frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Configure grid weights for center alignment
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# UI components
label_length = tk.Label(frame, text="Password Length:")
label_length.grid(row=0, column=0, pady=10, sticky="w")

entry_length = tk.Entry(frame)
entry_length.grid(row=0, column=1, pady=10)

var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

checkbox_uppercase = tk.Checkbutton(frame, text="Include Uppercase", variable=var_uppercase)
checkbox_uppercase.grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

checkbox_lowercase = tk.Checkbutton(frame, text="Include Lowercase", variable=var_lowercase)
checkbox_lowercase.grid(row=2, column=0, columnspan=2, sticky="w", padx=10)

checkbox_digits = tk.Checkbutton(frame, text="Include Digits", variable=var_digits)
checkbox_digits.grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

checkbox_symbols = tk.Checkbutton(frame, text="Include Symbols", variable=var_symbols)
checkbox_symbols.grid(row=4, column=0, columnspan=2, sticky="w", padx=10)

button_generate = tk.Button(frame, text="Generate Password", command=on_generate)
button_generate.grid(row=5, column=0, columnspan=2, pady=10)

label_result = tk.Label(frame, text="", width=30, height=2, relief="sunken")
label_result.grid(row=6, column=0, columnspan=2, pady=10)

button_copy = tk.Button(frame, text="Copy to Clipboard", command=on_copy)
button_copy.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
