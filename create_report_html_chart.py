#!/usr/bin/env python
import csv
import numpy as np
from sklearn.linear_model import LinearRegression
from string import Template

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
    chart_template = Template('''
    <html>
    <head>
        <title>Linear Regression Visualization</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <canvas id="myChart" width="400" height="400"></canvas>

        <script>
            var ctx = document.getElementById('myChart').getContext('2d');
            var xValues = $xValues;
            var yValues = $yValues;
            var regressionLine = [];

            for (var i = 0; i < xValues.length; i++) {
                regressionLine.push($slope * xValues[i] + $intercept);
            }

            var data = {
                labels: xValues,
                datasets: [
                    {
                        label: 'Data',
                        data: yValues,
                        backgroundColor: 'blue',
                    },
                    {
                        label: 'Regression Line',
                        data: regressionLine,
                        borderColor: 'red',
                        fill: false,
                    },
                ]
            };

            var options = {
                responsive: true,
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'X'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Y'
                        }
                    }
                }
            };

            var myChart = new Chart(ctx, {
                type: 'scatter',
                data: data,
                options: options
            });
        </script>
    </body>
    </html>
    ''')

    # Substitute the values into the chart template
    html_content = chart_template.substitute(
        xValues=x_values,
        yValues=y_values,
        slope=slope,
        intercept=intercept
    )

    # Write the chart HTML to a file
    with open('visualization.html', 'w') as html_file:
        html_file.write(html_content)

    print('Visualization generated successfully. Please open visualization.html in a web browser.')

# Prompt the user for the filename
print("PT Cakrawala Bima Instrument -- Creating report in html chartjs")
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
