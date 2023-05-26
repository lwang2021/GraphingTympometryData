import sys
import os
import csv
from lxml import etree
from frequency import tonePoint

if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
else:
    print("Invalid number of arguments provided.")
    exit(1)

current_directory = os.path.dirname(os.path.abspath(__file__))
data = [arg1]

tree = etree.parse(arg2)

root = tree.getroot()

ns = root.nsmap

try:
    for i in range(8):
        pressure = tree.findall('.//PeakPressure', namespaces=ns)[i].text
        data.append(pressure)
        if (i < 2):
            volume = tree.findall('.//Volume', namespaces=ns)[i].text
            gradient = tree.findall('.//PressureGradient', namespaces=ns)[i].text
            compliance = tree.findall('.//Compliance', namespaces=ns)[i].text
            data.append(volume)
            data.append(gradient)
            data.append(compliance)
except:
    print("An error occured, please confirm that your file is correctly formatted")
    exit(1)

csv_file = current_directory + "/Output Files/tympanogramOutput.csv"

existing_data = []
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    existing_data = list(reader)

existing_data.append(data)

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the data to the CSV file
    writer.writerows(existing_data)