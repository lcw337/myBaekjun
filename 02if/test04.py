def printQuadrant(xPos, yPos):
    if xPos>0:
        if yPos>0:
            print("1")
        else:
            print("4")
    else:
        if yPos>0:
            print("2")
        else:
            print("3")

xPos = int(input())
yPos = int(input())

printQuadrant(xPos, yPos)
