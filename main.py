#import necessary libraries

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from itertools import count

# Load your data into a DataFrame named 'data'
# Example: data = pd.read_csv('your_data.csv')

# Filter the data to start from 1990 and stop at 2018
data = data[(data['Year'] >= 1990) & (data['Year'] <= 2018)]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Set the x-axis limits and ticks (from 1990 to 2018 with a 3-year interval)
ax.set_xlim(1990, 2018)
ax.set_xticks(range(1990, 2019, 3))

# Initialize the y-axis limit and interval
y_min = 200
y_max = 5000
y_interval = 200

# Set the y-axis limits and ticks
ax.set_ylim(y_min, y_max)
ax.set_yticks(range(y_min, y_max + 1, y_interval))

# Define empty lists for x and y values
x_data, y1_data, y2_data = [], [], []

# Create an iterator for x values with a 3-year interval
x_vals = count(1990, 3)

# Function to animate the plot
def animate(i):
    x_val = next(x_vals)
    
    # Extract Gold and Dow Jones values for the current year
    year_data = data[data['Year'] == x_val]
    month_years = year_data['Month_Year'].tolist()
    gold_values = year_data['Gold']
    dow_jones_values = year_data['Dow Jones']
    
    # Update the plot with month-year combinations
    for month_year, gold, dow_jones in zip(month_years, gold_values, dow_jones_values):
        x_data.append(x_val)  # Consider appending unique x values if needed
        y1_data.append(gold)
        y2_data.append(dow_jones)

    # Update the plot
    ax.clear()
    ax.plot(x_data, y1_data, label='Gold', color='yellow', marker='o', markersize=6)
    ax.plot(x_data, y2_data, label='Dow Jones', color='orange', marker='o', markersize=6)
    
    # Set the title to display month and year
    ax.set_title(f"Year: {x_val}")
    ax.legend(loc='upper left', bbox_to_anchor=(0.98, 0.94))

# Create the animation
anim = FuncAnimation(fig, animate, interval=50)

# Show the plot
plt.show()
