# BMI Calculator with User Tracking and Visualization

This is an advanced Python project to calculate the Body Mass Index (BMI) of users, track their weight, height, and BMI over time, and visualize the data in interactive graphs. The application is built using the Tkinter library for the graphical user interface (GUI), Matplotlib for data visualization, and JSON for data storage.

## Features:
1. **User Tracking**:
   - Each user is identified by their name.
   - The application stores multiple users' data separately.
   - For each user, the weight, height, and BMI are recorded with a timestamp.

2. **BMI Calculation**:
   - Users input their weight (kg) and height (m).
   - The BMI is calculated using the standard formula:
     \[
     BMI = \frac{weight}{height^2}
     \]
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

## Installation:

### Prerequisites:
- Python 3.x
- Tkinter
- Matplotlib

To install the required dependencies, run:

```bash
pip install matplotlib
