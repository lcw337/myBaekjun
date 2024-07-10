numOfCard, targetNum = map(int, input().split())
cards = list(map(int, input().split()))


def isBest(currentSum):
    if bestSum < currentSum and targetNum >= currentSum:
        return True

bestSum = 0
#012~789니까
for i in range(0, numOfCard-2):
    for j in range(i+1, numOfCard-1):
        for k in range(j+1, numOfCard):
            currentSum = cards[i] + cards[j] + cards[k]
            if isBest(currentSum):
                bestSum = currentSum

print(bestSum)

