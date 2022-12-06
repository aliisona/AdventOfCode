file = open('Day1_input.txt', 'r')
 
# Reading from the file
Content = file.readlines()
 
totals = []
sum = 0;
countOfElves = 0
for line in Content: 
    if (line == "\n"):
        print(sum)
        totals.append(sum)
        sum = 0
    else:
        sum += int(line)
        countOfElves+=1

print(countOfElves)

max = 0
for i in range(len(totals)):
    if (totals[i]>max):
        max = totals[i]
        maxIndex = i
        print(maxIndex)

print("\n\n Max:", max, "\nIndex: ", maxIndex)

print(totals)
totalTop = 0
max1 = 0
max2 = 0
max3 = 0

maxes = []

print("\n\n")
for i in range(len(totals)):
    if (totals[i]>max3):
        max3 = totals[i]
        maxIndex3 = i
        maxes.append(max3)
        print(maxIndex3)

print(max3)

for i in range(len(totals)):
    if (totals[i]>max2 and totals[i] != max3):
        max2 = totals[i]
        maxIndex2 = i
        maxes.append(max2)
        print(maxIndex2)

print(max2)

for i in range(len(totals)):
    if (totals[i]>max1 and totals[i] != max2 and totals[i] != max3):
        max1 = totals[i]
        maxIndex1 = i
        maxes.append(max1)
        print(maxIndex1)

print(max1)

sumMaxes = 0
for i in range(len(maxes)):
    sumMaxes += maxes[i]

sumMaxes = max3 + max2 + max1
print("\n\n Totals:", sumMaxes)


