import sys
import lxml

if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
else:
    print("Invalid number of arguments provided.")
    exit(1)