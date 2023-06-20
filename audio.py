import sys
import os
import csv
from lxml import etree
from frequency import tonePoint

# Confirms the number of arguments inputted
if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
else:
    print("Invalid number of arguments provided.")
    exit(1)

# Initialization of variables
# Gets the directory that this file is in
current_directory = os.path.dirname(os.path.abspath(__file__))
rightAC = []
leftAC = []
rightBC = []
leftBC = []
data = [arg1]
earSide = None
conduction = None
frequency = None
masking = None
value = None
maskedValue = None

# Sets the XML tree to a variable
tree = etree.parse(arg2)
# Gets the namespace of the file
root = tree.getroot()
ns = root.nsmap

# Finds each section, and puts data in corresponding list

# Four <Tone> fields
# [0]: Right AC
# [1]: Left AC
# [2]: Right BC
# [3]: Left BC
unparsedData = tree.findall('.//Tone', namespaces=ns)[:4]

# Obtains the various parts of the file that we need by their tags
for tone in unparsedData:
    # Finds the side of the ear
    earSide = tone.find('Earside', namespaces=ns).text
    # Finds which type of conduction it is
    conduction = tone.find('ConductionTypes', namespaces=ns).text
    # Within this section, there's another called TonePoint
    # We now iterate through that
    for i in tone.findall('TonePoint', namespaces=ns):
        # Finds the frequency we're working with
        frequency = i.find('Frequency', namespaces=ns).text

        # Case 1: Not masked
        if (i.find('StatusUT', namespaces=ns).text == "Heard"):
            masking = False
            value = i.find('IntensityUT', namespaces=ns).text
        
        # Case 2: Masked
        elif (i.find('StatusMT', namespaces=ns).text == "Heard"):
            masking = True
            value = i.find('IntensityMT', namespaces=ns).text
            maskedValue = i.find('IntensityMTMasked', namespaces=ns).text
        
        # Places the values into the correct list
        # Refer to frequency.py for tonePoint class
        if (earSide == "Right") and (conduction == "IP"):
            rightAC.append(tonePoint(frequency, value, masking))
        elif (earSide == "Right") and (conduction == "BC"):
            rightBC.append(tonePoint(frequency, value, masking))
        elif (earSide == "Left") and (conduction == "IP"):
            leftAC.append(tonePoint(frequency, value, masking))
        elif (earSide == "Left") and (conduction == "BC"):
            leftBC.append(tonePoint(frequency, value, masking))
        else:
            print("Was not able to extract data properly, please make sure file is configured correctly.")
            print("Error with file: " + arg2)
            exit(1)

for thatList in [rightAC, rightBC, leftAC, leftBC]:
    if not thatList:
        thatList.append(tonePoint(0, 0, 0))

# Places the list values into the CSV file
# Places into the data list
for i in range(6):
    # Checks for all frequencies that we need
    frequency = str(250 * pow(2, i))
    for i in range(len(rightAC)):
        if (rightAC[i].frequency == frequency):
            data.append(rightAC[i].value)
            data.append(int(rightAC[i].masking))
            break
        elif (i == (len(rightAC) - 1)):
            data.append('')
            data.append('')
    if (int(frequency) != 8000):
        for i in range(len(rightBC)):
            if (rightBC[i].frequency == frequency):
                data.append(rightBC[i].value)
                data.append(int(rightBC[i].masking))
                break
            elif (i == (len(rightBC) - 1)):
                data.append('')
                data.append('')
    for i in range(len(leftAC)):
        if (leftAC[i].frequency == frequency):
            data.append(leftAC[i].value)
            data.append(int(leftAC[i].masking))
            break
        elif (i == (len(leftAC) - 1)):
            data.append('')
            data.append('')
    if (int(frequency) != 8000):
        for i in range(len(leftBC)):
            if (leftBC[i].frequency == frequency):
                data.append(leftBC[i].value)
                data.append(int(leftBC[i].masking))
                break
            elif (i == (len(leftBC) - 1)):
                data.append('')
                data.append('')

data.append(1)

# Writing to the CSV file 
csv_file = current_directory + "/Output Files/audiogramOutput.csv"

existing_data = []
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    existing_data = list(reader)

existing_data.append(data)

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the data to the CSV file
    writer.writerows(existing_data)