bestCase = [1, 1, 2, 2, 2, 8]
inputCase = list(map(int, input().split()))
result = []

for i in range(len(bestCase)):
    result.append(bestCase[i] - inputCase[i])

for r in result:
    print(r, end=' ')