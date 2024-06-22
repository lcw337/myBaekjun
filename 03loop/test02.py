def printPlusResult():
    for result in results:
        print(result)

T = int(input())
results = []

for i in range(1, T+1):
    A, B = map(int, input().split())
    results.append(A+B)
printPlusResult()