numOftry = int(input())

newStrings = []
for i in range(numOftry):
    count, oldString = input().split()
    newString = ""
    for i in range(0, len(oldString)):
        newString += oldString[i] * int(count)
    newStrings.append(newString)

for n in newStrings:
    print(n)