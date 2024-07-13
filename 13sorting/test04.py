n = int(input())
myArr = []
for _ in range(n):
    myArr.append(int(input()))

myArr.sort()

for a in myArr:
    print(a)