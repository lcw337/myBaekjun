myArr = []
for _ in range(5):
    myArr.append(int(input()))

def avg(arr):
    aSum = 0
    for a in arr:
        aSum += a
    return aSum / len(arr)

print(int(avg(myArr)))

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b
def sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = swap(arr[j], arr[j+1])

sort(myArr)
print(myArr[2])