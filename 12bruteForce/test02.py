totalSum = int(input())
results = []
def digits_sum(n):
    list_n = list(str(n))
    dSum = 0
    while list_n:
        dSum += int(list_n.pop())
    return dSum



for i in range(1, totalSum+1):
    if i + digits_sum(i) == totalSum:
        results.append(i)

if results:
    print(min(results))
else:
    print(0)