def findMin():
    min = ints[0]
    for oneInt in ints:
        if min > oneInt:
            min = oneInt
    return min

def findMax():
    max = ints[0]
    for oneInt in ints:
        if max < oneInt:
            max = oneInt
    return max
def printMinMax():
    print(findMin(), findMax())

numOfint = int(input())
ints = list(map(int, input().split()))
printMinMax()