def findMin():
    min = ints[0]
    for i in range(0, len(ints)):
        if min > ints[i]:
            min = ints[i]
    return min

def findMax():
    max = ints[0]
    for i in range(0, len(ints)):
        if max < ints[i]:
            max = ints[i]
    return max
def printMinMax():
    print(findMin(), findMax())

numOfint = int(input())
ints = list(map(int, input().split()))
printMinMax()