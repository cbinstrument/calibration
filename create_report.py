#!/usr/bin/env python

import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def read_data_from_csv(filename):
    x_values = []
    y_values = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            x_values.append(float(row[0]))
            y_values.append(float(row[1]))
    return x_values, y_values

def generate_linear_regression_summary(x_values, y_values):
    x = np.array(x_values).reshape(-1, 1)  # Reshape X values to a 2D array
    y = np.array(y_values)
    model = LinearRegression()  # Create a LinearRegression model
    model.fit(x, y)  # Fit the model to the data
    summary = f'Intercept: {model.intercept_}\n'
    summary += f'Coefficient: {model.coef_}\n'
    return summary

def generate_visualization(x_values, y_values, slope, intercept):
    sns.set_style("darkgrid")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x_values, y=y_values, label='Data')
    sns.lineplot(x=x_values, y=slope * np.array(x_values) + intercept, color='red', label='Linear Regression')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression Visualization')
    plt.legend()
    plt.show()

# Prompt the user for the filename
print("PT Cakrawala Bima Instrument -- Creating report")
print("-----------------------------------------------------------------")
csv_filename = input("Enter the CSV filename containing X and Y values: ")

# Read data from CSV
x_values, y_values = read_data_from_csv(csv_filename)

# Generate linear regression summary
summary = generate_linear_regression_summary(x_values, y_values)

# Print linear regression summary
print('Linear Regression Summary:')
print(summary)

# Generate visualization
slope, intercept = np.polyfit(x_values, y_values, 1)  # Calculate the slope and intercept of the regression line
generate_visualization(x_values, y_values, slope, intercept)
