f = open('rawData.txt', 'r')

lines = f.readlines()

for i in range(len(lines)):
    line = lines[i].strip()
    lines[i] = line

testData = False
left = []
isLeft = False
right = []
isRight = False

for line in lines:
    if line == "TestData":
        testData = True
        isLeft = False
        isRight = False
    elif testData:
        if line == "Left":
            isLeft = True
            testData = False
        if line == "Right":
            isRight = True
            testData = False
    elif isLeft:
        left.append(line)
    elif isRight:
        right.append(line)

leftx = []
lefty = []
rightx = []
righty = []

for i in range(len(left)):
    if (i % 2) == 0:
        leftx.append(left[i])
    else:
        lefty.append(left[i])

for i in range(len(right)):
    if (i % 2) == 0:
        rightx.append(right[i])
    else:
        righty.append(right[i])

f = open("results/leftx.txt", "w")
for line in leftx:
    f.write(line)
    f.write('\n')
f.close()

f = open("results/lefty.txt", "w")
for line in lefty:
    f.write(line)
    f.write('\n')
f.close()

f = open("results/rightx.txt", "w")
for line in rightx:
    f.write(line)
    f.write('\n')
f.close()

f = open("results/righty.txt", "w")
for line in righty:
    f.write(line)
    f.write('\n')
f.close()