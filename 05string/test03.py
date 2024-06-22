numOfTry = int(input())
myStrings = []
for _ in range(numOfTry):
    myStrings.append(input())

myNewStrings = []
for myString in myStrings:
    myNewStrings.append(myString[0]+myString[-1])

for myNewString in myNewStrings:
    print(myNewString)