inputNum = int(input())
primeFactors = []

num = 2
while inputNum > 1:
    if inputNum % num == 0:
        primeFactors.append(num)
        inputNum /= num
    else:
        num += 1

for primeFactor in primeFactors:
    print(primeFactor)
