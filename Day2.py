# file = open('Day2_input.txt', 'r')
# LineArr = file.readlines()
 
# #A - Rock
# #B - Paper
# #C - Scissors

# #X - Rock +1
# #Y - Paper +2
# #Z - Scissors +3

# #Win = 6
# #Lose = 0
# #Draw = 3

# #star 1``
# sum = 0
# def rockCalc(response):
#     global sum 
#     if response == "X":
#         sum+=(1 + 3)
#     if response == "Y":
#         sum+=2 + 6
#     if response == "Z":
#         sum+=(3)
# def paperCalc(response):
#     global sum
#     if response == "X":
#         sum+=(1)
#     if response == "Y":
#         sum+=(2 + 3)
#     if response == "Z":
#         sum+=3 + 6

# def scissorCalc(response):
#     global sum 
#     if response == "X":
#         sum+=1 + 6
#     if response == "Y":
#         sum+=(2)
#     if response == "Z":
#         sum+=(3 + 3)

# counter = 0
# for line in LineArr:
#     current = line[0]
#     response = line[2]

#     if current == "A":
#         rockCalc(response)
#     if current == "B":
#         paperCalc(response)
#     if current == "C":
#         scissorCalc(response)

#     print(line)
#     print(sum)
#     counter+=1

# print("\n\n", counter)
# print("\n\n", sum)


#star 2

file = open('Day2_input.txt', 'r')
LineArr = file.readlines()
 
#A - Rock - 1
#B - Paper - 2
#C - Scissors - 3

#X - Need to lose
#Y - Need to draw
#Z - Need to win

#Win = 6
#Lose = 0
#Draw = 3

sum = 0
def rockCalc(response):
    global sum 
    if response == "X":
        sum+=(3)
    if response == "Y":
        sum+=1 + 3
    if response == "Z":
        sum+=(2 + 6)
def paperCalc(response):
    global sum
    if response == "X":
        sum+=(1)
    if response == "Y":
        sum+=(2 + 3)
    if response == "Z":
        sum+=3 + 6

def scissorCalc(response):
    global sum 
    if response == "X":
        sum+= 2
    if response == "Y":
        sum+=(3 + 3)
    if response == "Z":
        sum+=(1 + 6)

counter = 0
for line in LineArr:
    current = line[0]
    response = line[2]

    if current == "A":
        rockCalc(response)
    if current == "B":
        paperCalc(response)
    if current == "C":
        scissorCalc(response)

    print(line)
    print(sum)
    counter+=1

print("\n\n", counter)
print("\n\n", sum)


     

