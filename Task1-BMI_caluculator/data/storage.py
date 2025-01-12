# data/storage.py
import json
from datetime import datetime

FILE_PATH = "data/user_data.json"

def save_data(user_data):
    with open(FILE_PATH, 'w') as file:
        json.dump(user_data, file)

def load_data():
    try:
        with open(FILE_PATH, 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return {}  # Return empty dict if file is empty
    except FileNotFoundError:
        return {}

def add_user_data(user_name, weight, height, bmi):
    user_data = load_data()

    # Create new user entry if user doesn't exist
    if user_name not in user_data:
        user_data[user_name] = []

    # Append new data for the user
    user_data[user_name].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "weight": weight,
        "height": height,
        "bmi": bmi
    })

    save_data(user_data)
