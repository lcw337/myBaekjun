def findNumCount():
    count = 0
    for i in range(0, numOfNumbers):
        if inputNumbers[i] == NumberToFind:
            count += 1
    return count
def printResult():
    print(findNumCount())

numOfNumbers = int(input())
inputNumbers = []
inputNumbers = list(map(int, input().split()))
NumberToFind = int(input())

printResult()