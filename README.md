# Python Projects

This repository contains multiple Python projects built with different libraries and frameworks. Below is an overview of the two main projects in this repository: **Weather App** ,**Random Password Generator** and **BMI Calculator with User Tracking and Visualization**.

---

##  1. Weather App

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





## 2. Random Password Generator

This is an **Advanced Random Password Generator** built using Python and Tkinter for the graphical user interface (GUI). The password generator allows users to specify their password requirements, such as length and character types (letters, digits, symbols). It also ensures that the generated passwords meet security rules and provides an easy way to copy the generated password to the clipboard.

### Features:
- **Password Length**: Users can define the desired length of the password.
- **Character Types**: Users can select whether to include:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Symbols
- **Security Rules**: The password generator ensures that the password is secure based on selected character types.
- **Clipboard Integration**: After generating a password, users can easily copy it to the clipboard for quick use.
- **Intuitive GUI**: The app features a user-friendly graphical interface built with Tkinter.

### Technologies Used:
- **Python**: Programming language.
- **Tkinter**: GUI library for building the application interface.
- **pyperclip**: Clipboard functionality to copy the generated password.
- **string**: For handling character sets (letters, digits, symbols).

### Setup Instructions:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/random-password-generator.git
    cd random-password-generator
    ```

2. Install the required dependencies:

    ```bash
    pip install pyperclip
    ```

3. Run the application:

    ```bash
    python main.py
    ```

---

## 3. BMI Calculator with User Tracking and Visualization

This is an advanced Python project to calculate the Body Mass Index (BMI) of users, track their weight, height, and BMI over time, and visualize the data in interactive graphs. The application is built using the Tkinter library for the graphical user interface (GUI), Matplotlib for data visualization, and JSON for data storage.

### Features:
1. **User Tracking**:
   - Each user is identified by their name.
   - The application stores multiple users' data separately.
   - For each user, the weight, height, and BMI are recorded with a timestamp.

2. **BMI Calculation**:
   - Users input their weight (kg) and height (m).
   - The BMI is calculated using the standard formula:
     \[ BMI = \frac{weight}{height^2} \]
   - The BMI is classified into categories:
     - Underweight: BMI < 18.5
     - Normal: 18.5 ≤ BMI < 24.9
     - Overweight: 25 ≤ BMI < 29.9
     - Obese: BMI ≥ 30

3. **Data Storage**:
   - All user data (weight, height, BMI, and date) is stored in a JSON file.
   - The program supports adding new user data and displaying existing user data.

4. **Visualization**:
   - A graph is displayed showing the trends of weight, height, and BMI over time for a specific user.
   - The graph contains three curves:
     - Weight (kg)
     - Height (m)
     - BMI
   - Weight and height are displayed on the left y-axis, while BMI is displayed on the right y-axis.

5. **Error Handling**:
   - Input validation to ensure that the user enters valid data.
   - Error handling for missing or corrupted data files.

### Technologies Used:
- **Python**: Programming language.
- **Tkinter**: GUI library for building the application interface.
- **Matplotlib**: For data visualization.
- **JSON**: For storing user data.
- **datetime**: For timestamping user data.

### Setup Instructions:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/bmi-calculator.git
    cd bmi-calculator
    ```

2. Install the required dependencies:

    ```bash
    pip install matplotlib
    ```

3. Run the application:

    ```bash
    python main.py
    ```

---


---

## Acknowledgements
- Tkinter documentation for creating the GUI.
- pyperclip library for clipboard functionality in the **Random Password Generator** project.
- Matplotlib for visualizations in the **BMI Calculator** project.

---

Feel free to explore each project, make modifications, and contribute!
