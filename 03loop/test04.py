realTotalPrice = 0
receiptTotalPrice = Price = int(input())
numOfObject = int(input())
for i in range(1, numOfObject+1):
    objPrice, objAmount = map(int, input().split())
    realTotalPrice += objPrice*objAmount
if receiptTotalPrice == realTotalPrice:
    print("Yes")
else:
    print("No")