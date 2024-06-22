numOfBaskets, numOfTries = map(int, input().split())
baskets = []
for i in range(numOfBaskets):
    baskets.append(i+1)


def reverseBasket(x, y):
    while x < y:
        baskets[x], baskets[y] = baskets[y], baskets[x]
        x += 1
        y -= 1


for _ in range(numOfTries):
    x, y = map(int, input().split())
    reverseBasket(x-1, y-1) #인덱스로 보냄

for basket in baskets:
    print(basket, end=" ")