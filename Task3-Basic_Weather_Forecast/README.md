# Weather App

A simple weather application built with Python using Tkinter for the graphical user interface (GUI). The app allows users to check current weather details by entering a city name. It includes weather icons, unit conversion (Celsius/Fahrenheit), and smooth animations for a better user experience.

## Features

- **Current Weather**: Displays current weather details like temperature, humidity, and description.
- **Weather Icons**: Fetches and displays weather icons based on the weather conditions.
- **Unit Conversion**: Toggle between Celsius and Fahrenheit for temperature readings.
- **Error Handling**: Handles errors such as invalid city input or API issues gracefully.
- **Animated GUI**: Smooth transitions and weather data updates.

## Technologies Used

- **Python**: Programming language.
- **Tkinter**: GUI library for building the application interface.
- **OpenWeatherMap API**: Fetches weather data (temperature, humidity, weather conditions, etc.).
- **Pillow (PIL)**: Used to handle and display weather icons.
- **Requests**: For making HTTP requests to the OpenWeatherMap API.

## Setup Instructions

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies

To install the required libraries, run the following command:

```bash
pip install requests Pillow
```


api_key = "your_actual_api_key_here"  # Replace with your actual API key


python src/app.py
