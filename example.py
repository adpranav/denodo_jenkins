import csv
import os

# 1. Define the file path and file name
folder_path = r"C:\Users\adpra\OneDrive\Desktop\Data\Denodo"
file_name = "flight_details.csv"
full_path = os.path.join(folder_path, file_name)

# 2. Create the directory if it doesn't exist (Safety check)
os.makedirs(folder_path, exist_ok=True)

# 3. Define the flight data
headers = ["Flight_ID", "Airline", "Origin", "Destination", "Departure_Time", "Status"]
data = [
    ["AI-101", "Air India", "DEL", "JFK", "02:00", "On Time"],
    ["BA-245", "British Airways", "LHR", "BOM", "10:15", "Delayed"],
    ["EK-505", "Emirates", "DXB", "BLR", "14:30", "Boarding"],
    ["LH-789", "Lufthansa", "FRA", "SIN", "22:00", "Scheduled"],
    ["UA-044", "United", "SFO", "EWR", "06:45", "Cancelled"],
    ["UA-045", "United", "SFO", "VTZ", "06:45", "Boarding"]
]

# 4. Write to the CSV file
try:
    with open(full_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write the header row
        writer.writerows(data)    # Write the data rows
    
    print(f"Success! File created at: {full_path}")

except PermissionError:
    print("Error: Permission denied. Please close the file if it is currently open.")
except Exception as e:
    print(f"An error occurred: {e}")
