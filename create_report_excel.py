#!/usr/bin/env python
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.utils.dataframe import dataframe_to_rows

def read_data_from_csv(filename):
    x_values = []
    y_values = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            try:
                x_values.append(float(row[0]))
                y_values.append(float(row[1]))
            except ValueError:
                continue
    return x_values, y_values

def generate_linear_regression_summary(x_values, y_values):
    if len(x_values) == 0 or len(y_values) == 0:
        return "Insufficient data points for linear regression."
    
    x = np.array(x_values).reshape(-1, 1)  # Reshape X values to a 2D array
    y = np.array(y_values)
    model = LinearRegression()  # Create a LinearRegression model
    model.fit(x, y)  # Fit the model to the data
    intercept = model.intercept_
    coefficient = model.coef_[0]
    summary = f'Intercept: {intercept}\nCoefficient: {coefficient}'
    return summary

# Prompt the user for the CSV filename and output filename
print("PT Cakrawala Bima Instrument -- Creating report in excel file")
print("-----------------------------------------------------------------")
csv_filename = input("Enter the CSV filename containing X and Y values: ")
excel_filename = input("Enter the filename to save the trendline chart and summary (include .xlsx extension): ")

# Read data from CSV
x_values, y_values = read_data_from_csv(csv_filename)

# Generate linear regression summary
summary = generate_linear_regression_summary(x_values, y_values)

# Check if there are sufficient data points for linear regression
if summary == "Insufficient data points for linear regression.":
    print(summary)
    exit()

# Create a DataFrame for saving to Excel
data = {'X': x_values, 'Y': y_values}
df = pd.DataFrame(data)

# Create an Excel workbook and add the data
workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'Data'

# Write the header row
worksheet['A1'] = 'X'
worksheet['B1'] = 'Y'

# Write the data rows
for i, (x, y) in enumerate(zip(x_values, y_values), start=2):
    worksheet[f'A{i}'] = x
    worksheet[f'B{i}'] = y

# Generate trendline using linear regression
slope, intercept = np.polyfit(x_values, y_values, 1)  # Calculate the slope and intercept of the trendline
trendline = slope * np.array(x_values) + intercept

# Plot the data points and trendline using seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x_values, y=y_values, label='Data')
sns.lineplot(x=x_values, y=trendline, color='red', label='Trendline')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trendline Chart - CBI Calibration')
plt.legend()
chart_filename = 'chart.png'
plt.savefig(chart_filename)
plt.close()

# Add the chart image to the worksheet
img = Image(chart_filename)
img.anchor = 'D1'
worksheet.add_image(img)

# Add the linear regression summary to the worksheet
summary_sheet = workbook.create_sheet('Summary')
summary_sheet['A1'] = 'Linear Regression Summary'
summary_sheet['A2'] = summary

# Save the workbook to Excel file
workbook.save(excel_filename)

print("Trendline chart and summary have been generated and saved.")
