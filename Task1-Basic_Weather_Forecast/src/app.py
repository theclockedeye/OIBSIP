# /src/app.py
import tkinter as tk
from gui import WeatherApp

def main():
    root = tk.Tk()
    api_key = "8ef23515072798b7b45a5bf64ebbb774"  # Replace with your actual API key
    app = WeatherApp(root, api_key)
    root.mainloop()

if __name__ == "__main__":
    main()
