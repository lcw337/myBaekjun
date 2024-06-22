def printOneLine(i):
    for i in range(1, i+1):
        print("*", end="")
def printStars(numOfLine):
    for i in range(1, numOfLine+1):
        printOneLine(i)
        print("")

numOfLine = int(input())
printStars(numOfLine)