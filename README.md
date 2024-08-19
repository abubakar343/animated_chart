# Animated Line Chart Visualization

## Overview

This script generates an animated line chart that visualizes data over time, specifically focusing on the trends of two variables, such as Gold prices and Dow Jones index values. The data is filtered to cover the years between 1990 and 2018, and the animation shows the progression of these values across this time period.

## Features

- **Data Filtering**: The script filters the dataset to include only the years between 1990 and 2018.
- **Animated Plot**: An animated line chart is generated, showing the progression of Gold prices and Dow Jones index values over time.
- **Interactive Visualization**: The plot is created using Matplotlib with the Qt5Agg backend, allowing for interactive features.

## Code Explanation

### 1. Import Required Libraries
The script imports necessary libraries such as `matplotlib`, `pandas`, `numpy`, and others to handle data and create the visualization.

### 2. Data Filtering
The data is filtered to include only the years between 1990 and 2018. This ensures that the plot focuses on the desired time range.

### 3. Plot Setup
- **Figure and Axis**: A figure and axis are created using Matplotlib.
- **Axis Configuration**: The x-axis is set to range from 1990 to 2018 with a 3-year interval. The y-axis is set with custom limits and intervals based on the data's range.
- **Data Initialization**: Empty lists are initialized to store x and y values for the animation.

### 4. Animation Function
The `animate` function updates the plot with new data points at each frame. It iterates through the data for each year, appending new data points to the plot and updating the chart with markers for Gold and Dow Jones values.

### 5. Animation Creation
The `FuncAnimation` class from Matplotlib is used to create the animation, which updates the plot at a specified interval.

### 6. Display the Plot
The plot is displayed using `plt.show()`, which renders the animated chart in an interactive window.

## How to Use

1. **Install Required Libraries**:
   Ensure you have the required Python libraries installed. You can install them using pip:
   ```bash
   pip install matplotlib pandas numpy
   ```

2. **Prepare Your Data**:
   - Load your data into a DataFrame named `data`.
   - Ensure your data includes a 'Year' column, along with columns for the variables you want to plot (e.g., 'Gold' and 'Dow Jones').

3. **Run the Script**:
   Execute the script to generate the animated line chart. The chart will display in an interactive window, showing the progression of the selected variables over time.

## Acknowledgments

This code was developed with the help of various resources and documentation available online, particularly focusing on creating animated visualizations using Matplotlib.
