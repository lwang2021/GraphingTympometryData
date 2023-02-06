#!/bin/bash

filename=$(ls ./files | grep xml)

awk -F'[<>]' '/<XYDataOrigin>/ || /<EarSide>/ || /<X>/ || /<Y>/ {print $3}' "./Files/$filename" > rawData.txt

py read.py

awk -F'[<>]' '/<PeakPressure>/ {print $3}' "./Files/$filename" > rawData.txt

py peakPressure.py