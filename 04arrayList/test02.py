def findUnders():
    for i in range(0, numOfSequences):
        if targetNumber>sequences[i]:
            underNumbers.append(sequences[i])



numOfSequences, targetNumber = map(int, input().split())
sequences = list(map(int, input().split()))
underNumbers = []
findUnders()
for i in range(0, len(underNumbers)):
    print(underNumbers[i], end=" ")