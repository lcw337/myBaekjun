sugar = int(input())
numOfBag = 0
while sugar != 0:
    if sugar % 5 == 0:
        numOfBag += sugar//5
        sugar = 0
    else:
        sugar -= 3
        numOfBag += 1
    if sugar < 0:
        numOfBag = -1
        break

print(numOfBag)

