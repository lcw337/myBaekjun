inputs = list(map(int, input().split()))
divs = []
for i in range(1, inputs[0]+1):
    if inputs[0] % i == 0:
        divs.append(i)

target = inputs[1] - 1

try:
    print(divs[target])
except IndexError:
    print(0)