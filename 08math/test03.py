target = int(input())
rangeMax = 1
calCount = 1

while target > rangeMax:   #범위의최댓값과 비교해 구간찾음
    rangeMax += 6*calCount
    calCount += 1

print(calCount)
