def printOneLine(i):
    for k in range(1, numOfLine - i+1):
        print(" ", end="")
    for j in range(1, i+1):
        print("*", end="")
def printStars():
    for i in range(1, numOfLine+1):
        printOneLine(i)
        print("")

numOfLine = int(input())
printStars()