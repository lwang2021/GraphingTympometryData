f = open('rawData.txt', 'r')

lines = f.readlines()

f.close()

for i in range(len(lines)):
    line = lines[i].strip()
    lines[i] = line

f = open('results/peakPressure.txt', 'w')
f.write("Left\n")

for i in range(len(lines)):
    if i <= 2:
        f.write(lines[i] + '\n')
        
f.write("Right\n")

for i in range(len(lines)):
    if i > 2:
        f.write(lines[i] + '\n')
