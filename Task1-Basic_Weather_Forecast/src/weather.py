# /src/weather.py
import requests

class WeatherAPI:
    def __init__(self, api_key, units="metric"):
        self.api_key = api_key
        self.units = units
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, location):
        url = f"{self.base_url}?q={location}&units={self.units}&appid={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            main = data['main']
            weather = data['weather'][0]
            temp = main['temp']
            humidity = main['humidity']
            description = weather['description']
            icon = weather['icon']
            return temp, humidity, description, icon
        else:
            # Handle error if API fetch fails
            error_message = data.get('message', 'Unable to fetch data')
            print(f"Error fetching weather data: {error_message}")
            return None
