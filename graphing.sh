#!/bin/bash

awk -F'[<>]' '/<XYDataOrigin>/ || /<EarSide>/ || /<X>/ || /<Y>/ {print $3}' "./Files/Test4.xml" > rawData.txt

py read.py

awk -F'[<>]' '/<PeakPressure>/ {print $3}' "./Files/Test4.xml" > rawData.txt

py peakPressure.py