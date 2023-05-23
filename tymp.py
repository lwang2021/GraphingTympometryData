import sys
import lxml

if len(sys.argv) >= 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    print("RecordID", arg1, "file name", arg2)
else:
    print("Insufficient arguments provided.")