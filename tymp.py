import sys
import os
import csv
from lxml import etree

# Confirms the number of arguments inputted
if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
else:
    print("Invalid number of arguments provided.")
    exit(1)

# Gets the directory that this file is in
current_directory = os.path.dirname(os.path.abspath(__file__))
data = [arg1]

# Sets the XML tree to a variable
tree = etree.parse(arg2)
# Gets the namespace of the file
root = tree.getroot()
ns = root.nsmap

try:
    # We want all the PeakPressure values
    # i = 0, 1: Tymp results
    # i = 3-7: P1-3 for each ear
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
# Checking for errors
except:
    print("An error occured, please confirm that your file is correctly formatted")
    exit(1)

# Writing to the CSV file
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