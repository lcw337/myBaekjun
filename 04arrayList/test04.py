def printMax():
    print(max(inputNumbers))

def printMaxIndex():
    print(inputNumbers.index(max(inputNumbers))+1)
inputNumbers = []
for i in range(1, 10):
    inputNumbers.append(int(input()))
printMax()
printMaxIndex()
