# data/visualization.py
import matplotlib.pyplot as plt

def plot_user_data(user_data, user_name):
    if user_name not in user_data or not user_data[user_name]:
        return  # No data to display

    data = user_data[user_name]
    dates = [entry['date'] for entry in data]
    weights = [entry['weight'] for entry in data]
    heights = [entry['height'] for entry in data]
    bmis = [entry['bmi'] for entry in data]

    # Create figure and axis for plotting
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot Weight and Height on the primary y-axis
    ax1.plot(dates, weights, marker='o', color='blue', label='Weight (kg)')
    ax1.plot(dates, heights, marker='o', color='green', label='Height (m)')
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Weight (kg) & Height (m)", color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    # Create secondary y-axis for BMI
    ax2 = ax1.twinx()
    ax2.plot(dates, bmis, marker='o', color='red', label='BMI')
    ax2.set_ylabel("BMI", color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Add titles and labels
    ax1.set_title(f'{user_name} - Weight, Height & BMI Over Time')

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)

    # Add legends for each curve
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Layout adjustments
    plt.tight_layout()

    # Show the plot
    plt.show()
