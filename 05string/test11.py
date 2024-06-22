#main
phoneNums = list(input())


def changeToNums(phoneNums):
    for i in range(len(phoneNums)):
        if phoneNums[i] in 'ABC':
            phoneNums[i] = 2
        elif phoneNums[i] in 'DEF':
            phoneNums[i] = 3
        elif phoneNums[i] in 'GHI':
            phoneNums[i] = 4
        elif phoneNums[i] in 'JKL':
            phoneNums[i] = 5
        elif phoneNums[i] in 'MNO':
            phoneNums[i] = 6
        elif phoneNums[i] in 'PQRS':
            phoneNums[i] = 7
        elif phoneNums[i] in 'TUV':
            phoneNums[i] = 8
        elif phoneNums[i] in 'WXYZ':
            phoneNums[i] = 9
        else:
            print("Error")



changeToNums(phoneNums)


def getTime(phoneNums):
    time = 0
    for i in range(len(phoneNums)):
        time += phoneNums[i] + 1
    return time

time = getTime(phoneNums)
print(time)