file = open('Day6_input.txt', 'r')
 
# Reading from the file
Content = file.readlines()
def checkDif(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    return True

charCount = 0 
startSub = 0
for line in Content:
    for i in range(len(line)+14):
        charCount+=1
        subStringCheck = line[startSub:(startSub+14)]
        print(subStringCheck, checkDif(subStringCheck), "\n")
        if checkDif(subStringCheck):
            print(startSub)
            break
        else:
            startSub+=1

print(charCount+13)
 
