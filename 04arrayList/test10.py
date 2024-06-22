numOfSubjects = int(input())
scores = [0] * numOfSubjects
scores = list(map(int, input().split()))

maxScore = max(scores)
myNewScores = [0] * numOfSubjects

for i in range(numOfSubjects):
    myNewScores[i] = scores[i] / maxScore * 100

myNewAvg = sum(myNewScores) / numOfSubjects
print(myNewAvg)