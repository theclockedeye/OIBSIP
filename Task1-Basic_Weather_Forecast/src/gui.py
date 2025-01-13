# /src/gui.py
import tkinter as tk
from tkinter import messagebox
from weather import WeatherAPI
from PIL import Image, ImageTk
import requests
from io import BytesIO

class WeatherApp:
    def __init__(self, master, api_key):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        self.api_key = api_key
        self.units = "metric"  # Default to Celsius

        # Widgets
        self.city_label = tk.Label(master, text="Enter city:", font=("Arial", 12))
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(master, font=("Arial", 12), width=20)
        self.city_entry.pack(pady=5)

        self.fetch_button = tk.Button(master, text="Get Weather", command=self.fetch_weather, font=("Arial", 12))
        self.fetch_button.pack(pady=10)

        self.unit_button = tk.Button(master, text="Switch to Fahrenheit", command=self.toggle_units, font=("Arial", 12))
        self.unit_button.pack(pady=5)

        self.weather_info = tk.Label(master, text="", font=("Arial", 12))
        self.weather_info.pack(pady=10)

        self.weather_icon_label = tk.Label(master)
        self.weather_icon_label.pack(pady=10)

    def fetch_weather(self):
        location = self.city_entry.get()
        if location:
            self.get_weather(location)
        else:
            messagebox.showerror("Input Error", "Please enter a city name.")

    def get_weather(self, location):
        weather_api = WeatherAPI(self.api_key, self.units)
        weather_data = weather_api.get_weather(location)

        if weather_data:
            temp, humidity, description, icon = weather_data
            weather_details = f"Temp: {temp:.2f}°\nHumidity: {humidity}%\nCondition: {description.capitalize()}"

            # Set weather text
            self.weather_info.config(text=weather_details)

            # Fetch and display weather icon
            icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
            self.display_icon(icon_url)
        else:
            messagebox.showerror("Error", "Unable to fetch weather data.")

    def display_icon(self, icon_url):
        try:
            # Fetch the icon image
            response = requests.get(icon_url)
            img_data = response.content
            image = Image.open(BytesIO(img_data))

            # Resize and display the image in Tkinter
            image = image.resize((50, 50), Image.ANTIALIAS)
            tk_image = ImageTk.PhotoImage(image)
            self.weather_icon_label.config(image=tk_image)
            self.weather_icon_label.image = tk_image
        except Exception as e:
            print(f"Error loading icon: {e}")

    def toggle_units(self):
        if self.units == "metric":  # Celsius
            self.units = "imperial"  # Fahrenheit
            self.unit_button.config(text="Switch to Celsius")
        else:
            self.units = "metric"  # Celsius
            self.unit_button.config(text="Switch to Fahrenheit")

        self.fetch_weather()  # Re-fetch the weather with the updated units
