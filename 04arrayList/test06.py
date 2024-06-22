numOfbaskets, numOftries = map(int, input().split())
baskets = []
for i in range(0, numOfbaskets):
    baskets.append(i+1)

def swap(x, y):
    baskets[x-1], baskets[y-1] = baskets[y-1], baskets[x-1]

for _ in range(numOftries):
    x, y = map(int, input().split())
    swap(x,y)

for basket in baskets:
    print(basket, end=" ")