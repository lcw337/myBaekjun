numOfTry = int(input())

myArr = []
for _ in range(numOfTry):
    myArr.append(int(input()))

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def bubbleSort(arr):
    for i in range(len(arr)-1): #꼴찌 카운트용
        for j in range(len(arr)-1-i): #꼴지확정된거만큼뻄
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = swap(arr[j], arr[j+1])

bubbleSort(myArr)


for m in myArr:
    print(m)