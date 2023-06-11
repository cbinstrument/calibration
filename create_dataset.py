#!/usr/bin/env python

import os
import csv
import time
import pytz
from datetime import datetime

def collect_data(interval, duration):
    data = []
    end_time = time.time() + duration * 60  # Calculate end time based on duration in minutes
    while time.time() < end_time:
        jakarta_timezone = pytz.timezone('Asia/Jakarta')
        current_time = datetime.now(tz=jakarta_timezone)
        current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        os.system("echo '\a'")
        print(f"Current time in Jakarta: {current_time_str}")
        x = input("Enter the x value: ")
        y = input("Enter the y value: ")
        data.append([x, y])
        time.sleep(interval * 60)  # Sleep for the specified interval in minutes
    return data

def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y'])  # Write header row
        writer.writerows(data)

# Prompt the user for the input values
print("PT Cakrawala Bima Instrument -- Creating dataset")
print("-----------------------------------------------------------------")
interval = float(input("Enter the interval in minutes: "))
duration = float(input("Enter the duration in minutes: "))
filename = input("Enter the filename to save the data (include .csv extension): ")
print("-----------------------------------------------------------------")

# Collect data
data = collect_data(interval, duration)

# Save data to CSV
save_to_csv(filename, data)

print(f"Data has been saved to {filename}.")
