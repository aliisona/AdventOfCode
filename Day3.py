# file = open('Day3_input.txt', 'r')
# LineArr = file.readlines()

# matchedVals = []
# counter = 0

# for line in LineArr:
#     middle = int(len(line)/2)
#     half_1 = line[:middle]
#     half_2 = line[middle : (len(line))]

#     print(line)
#     print(half_1)
#     print(half_2)

#     counter+=1

#     for char in half_1:
#         if (char in half_2):
#             matchedVals.append(char)
#             break
    
# sums = []
# sum = 0

# for char in matchedVals:
#     charCode = ord(char)
#     toAdd = 0
#     if (char.islower()):
#         toAdd += (charCode - 96)
#     if (char.isupper()):
#         toAdd += (charCode - 64) + 26
#     sum+= toAdd
#     sums.append(toAdd)

# print(matchedVals)
# print(sums)
# print(counter)
# print("\n\n", sum)


#TWO
file = open('Day3_input.txt', 'r')
LineArr = file.readlines()

matchedVals = []
counter = 0

totalGroups = int(len(LineArr)/3)
print(totalGroups)

for group in range(0,totalGroups):
    r1 = LineArr[0 + 3*(group)]  
    r2 = LineArr[1 + 3*(group)] 
    r3 = LineArr[2 + 3*(group)]  

    print(r1)
    print(r2)
    print(r3)

    print("\n")

    for char in r1:
        if (char in r2 and char in r3):
                matchedVals.append(char)
                break

    counter+=1
    
sums = []
sum = 0
for char in matchedVals:
    charCode = ord(char)
    toAdd = 0
    if (char.islower()):
        toAdd += (charCode - 96)
    if (char.isupper()):
        toAdd += (charCode - 64) + 26
    sum+= toAdd
    sums.append(toAdd)

print(matchedVals)
print(sums)
print(counter)
print("\n\n", sum)




