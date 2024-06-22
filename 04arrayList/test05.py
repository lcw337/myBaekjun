def shareBall(startBasket, endBasket, baskets, ballNumber):
    for i in range(startBasket, endBasket+1):
        baskets[i-1] = ballNumber

def printBallAmount():
    for basket in baskets:
        print(basket, end=" ")


numOfBasket, numOfTry = map(int, input().split())
baskets = [0] * numOfBasket
for _ in range(numOfTry):   #인덱스아니면 i안씀
    startBasket, endBasket, ballNumber = map(int, input().split())
    shareBall(startBasket, endBasket, baskets, ballNumber)
printBallAmount()