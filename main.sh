#!/bin/bash

currentPath=$(dirname "$(realpath "$0")")

cp $currentPath/audiogramTemplate.csv $currentPath/"Output Files"/audiogramOutput.csv
cp $currentPath/tympanogramTemplate.csv $currentPath/"Output Files"/tympanogramOutput.csv

cd $currentPath/"Input Files"

filesPath=$(pwd)

IFS=$'\n'

unparsedDirectories=("$(find "$filesPath" -mindepth 1 -type d -execdir basename {} \;)")

directories=()
while IFS= read -r line; do
    directories+=("$line")
done <<< "$unparsedDirectories"

for dir in "${directories[@]}"; do

    let patientNum=$dir

    if [ $patientNum -le 0 ]; then
        echo "Please number (all) your patients with a valid Record ID"
        echo "Valid Record IDs are strictly greater than 0"
        echo "Try again once you have"
        exit 1
    fi

    cd $dir
    patientPath=$(pwd)

    extension=".xml"
    pattern1="tymp"
    pattern2="audio"

    tympPath=$(find "$patientPath" -type f -iname "*$pattern1*$extension" -print)
    audioPath=$(find "$patientPath" -type f -iname "*$pattern2*$extension" -print)

    python3 $currentPath/tymp.py $patientNum "$tympPath"
    python3 $currentPath/audio.py $patientNum "$audioPath"

    cd ..
done