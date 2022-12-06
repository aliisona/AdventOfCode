#STAR 1
# file1 = open('Day5_input.txt', 'r')
# InstructionsArr = file1.readlines()

# file2 = open('Day5_input2.txt', 'r')
# StackValues = file2.readlines()

# def getInstructions():
#     instructions = []
#     for line in InstructionsArr:
#         instructions.append([int(s) for s in line.split() if s.isdigit()])
        
#     return instructions
    
# print("instructions", getInstructions())

# def move(amount, fromstack, destination):
#     print("amount moving", amount)
#     print("from", fromstack)
#     print("to", destination)

#     for x in range(amount):
#         destination.insert(0, fromstack[0])
#         fromstack.pop(0)

# instructions = getInstructions()

# for instruction in instructions:
#     instruction[1] = instruction[1]-1
#     instruction[2] = instruction[2]-1

# print("new instructions", instructions)

# allStacks = []
# for line in StackValues: 
#     thisStack = []
#     for i in line: 
#         if i == "\n":
#             break
#         thisStack.append(i)
#     allStacks.append(thisStack)

# print("allStacks", allStacks)

# curIns = 0
# for line in getInstructions():
#     curInsLine = instructions[curIns]
    
#     print("\n")
#     print("Current Instruction", curInsLine)
#     print("Step", curIns+1, " ", allStacks)
#     move(curInsLine[0], allStacks[curInsLine[1]], allStacks[curInsLine[2]])
#     print("Stacks", allStacks)
#     curIns +=1

# topOfStacks = ""
# for stack in allStacks:
#     topOfStacks += stack[0]

# print("\n\nActions:", curIns)
# print(allStacks)
# print(topOfStacks)

#STAR TWO
file1 = open('Day5_input.txt', 'r')
InstructionsArr = file1.readlines()

file2 = open('Day5_input2.txt', 'r')
StackValues = file2.readlines()

def getInstructions():
    instructions = []
    for line in InstructionsArr:
        instructions.append([int(s) for s in line.split() if s.isdigit()])
        
    return instructions
    
print("instructions", getInstructions())


def move(amount, fromstack, destination):
    print("amount moving", amount)
    print("from", fromstack)
    print("to", destination)

    toAdd = []

    for x in range(amount):
        toAdd.insert(0, fromstack[0])
        fromstack.pop(0)

    print("Adding: ", toAdd)
    
    for c in toAdd:
        destination.insert(0, c)


instructions = getInstructions()

for instruction in instructions:
    instruction[1] = instruction[1]-1
    instruction[2] = instruction[2]-1

print("new instructions", instructions)

allStacks = []
for line in StackValues: 
    thisStack = []
    for i in line: 
        if i == "\n":
            break
        thisStack.append(i)
    allStacks.append(thisStack)

print("allStacks", allStacks)

curIns = 0
for line in getInstructions():
    curInsLine = instructions[curIns]
    
    print("\n")
    print("Current Instruction", curInsLine)
    print("Step", curIns+1, " ", allStacks)
    move(curInsLine[0], allStacks[curInsLine[1]], allStacks[curInsLine[2]])
    print("Stacks", allStacks)
    curIns +=1

topOfStacks = ""
for stack in allStacks:
    topOfStacks += stack[0]

print("\n\nActions:", curIns)
print(allStacks)
print(topOfStacks)

