# Writing XML Data into CSV Files
Currently supports Tympanogram, Audiogram, and William's Test results.

## Usage
1. Place patient files into the folder labelled "Input Files"
Note that these files should be the numbered ones, so inside the folder "Input Files" there should be folders, 001, 002, etc.

2. Copy the path of this folder.

3. In bash, type:

> sh (Your folder's path)/main.sh

4. Let the program run, this might take some time.

5. In "Output Files," you should see two files, upload both of these separately.

## File Configuration
In each of the patient folders, please make sure there is:

1. Only ONE file for tympanometry and that should be labelled tymp somewhere in the name, with the file extension ".xml"

2. Only ONE file for the audiogram and that should be labelled audio somewhere in the name, with the file extension ".xml"