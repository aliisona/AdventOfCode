file = open('Day4_input.txt', 'r')
LineArr = file.readlines()

def getList(asgn):
    middleBound = asgn.index('-')
    lowerBound = int(asgn[:(middleBound)])
    upperBound = int(asgn[(middleBound+1) : len(asgn)])

    asgnNum = []
    count = lowerBound
    for i in range(lowerBound, upperBound+1):
        asgnNum.append(count)
        count+=1

    return asgnNum

def checkForOverlap(list1, list2):
    for c in list1:
        if c in list2:
            return True
    return False

counter = 0
samePair = 0
overlaps = 0
for line in LineArr:
    counter+=1
    asgnBreak = line.index(',')

    asgn1 = line[:(asgnBreak)]
    asgn2 = line[(asgnBreak+1) : (len(line))]

    print(line)
    print(asgn1, asgn2, asgnBreak)

    asgn1_list = getList(asgn1)
    asgn2_list = getList(asgn2)

    print(asgn1_list, asgn2_list)

    if set(asgn1_list).issubset(set(asgn2_list)) or set(asgn2_list).issubset(set(asgn1_list)):
        samePair+=1

    if checkForOverlap(asgn1_list, asgn2_list):
        overlaps+=1


print("\n\ncounted:", counter)
print("pairs:", samePair)
print("overlaps:", overlaps)

#javascript animation, python, r, java, c#, c++, html, javascript, css, sql, matlab, swift, swiftUI, c shell