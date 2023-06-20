#!/bin/bash

# Gets the current directory that this file is in
currentPath=$(dirname "$(realpath "$0")")

# Makes a copy of the template
cp $currentPath/audiogramTemplate.csv $currentPath/"Output Files"/audiogramOutput.csv
cp $currentPath/tympanogramTemplate.csv $currentPath/"Output Files"/tympanogramOutput.csv

# Looks into the input files
cd $currentPath/"Input Files"

filesPath=$(pwd)

# Changes the delimiter
IFS=$'\n'

# Gets all of the patients in the input files
unparsedDirectories=("$(find "$filesPath" -mindepth 1 -type d -execdir basename {} \;)")

# Puts all of the directories into a list
directories=()
while IFS= read -r line; do
    directories+=("$line")
done <<< "$unparsedDirectories"

# For each patient...
for dir in "${directories[@]}"; do

    # Converts it into an integer
    let patientNum=$(echo "$dir" | sed 's/^0*//')

    # Checking for errors
    if [ $patientNum -le 0 ]; then
        echo "Please number (all) your patients with a valid Record ID"
        echo "Valid Record IDs are strictly greater than 0"
        echo "Try again once you have"
        exit 1
    fi

    # Goes into the patient folder
    cd $dir
    patientPath=$(pwd)

    extension=".xml"
    pattern1="tymp"
    pattern2="audio"

    # Searches for the correct file in the folder
    tympPath=$(find "$patientPath" -type f -iname "*$pattern1*$extension" -print)
    audioPath=$(find "$patientPath" -type f -iname "*$pattern2*$extension" -print)

    # Calls the corresponding python file with the given file
    python3 $currentPath/tymp.py $patientNum "$tympPath"
    python3 $currentPath/audio.py $patientNum "$audioPath"

    # Move back out to the general folder for the next patient
    cd ..
done