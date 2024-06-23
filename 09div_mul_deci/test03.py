inputs = []

while True:
    data = int(input())
    if data == -1:
        break
    inputs.append(data)
#print(inputs)

all_divs = []
for inp in inputs:
    divs = []
    for i in range(1, inp):
        if inp % i == 0:
            divs.append(i)
    all_divs.append(divs)
#print(all_divs)

isPerfects = []
for divs,inp in zip(all_divs,inputs):
    if sum(divs) == inp:
        isPerfect = True
    else:
        isPerfect = False
    isPerfects.append(isPerfect)


def printResult():
    for isPerfect,divs,inp in zip(isPerfects,all_divs,inputs):
        if isPerfect == True:
            print(inp, "= ", end="")
            for i in range(len(divs)):
                print(divs[i], end="")
                if i != len(divs)-1:    #마지막인덱스
                    print(" + ", end="")
            print()
        else:
            print(inp, "is NOT perfect.")
printResult()



