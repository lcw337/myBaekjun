numOfNumbers = int(input())
numbers = list(map(int, input().split()))

def isPrime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def isAllPrime(numbers):
    count = 0
    for number in numbers:
        if isPrime(number) == True:
            count += 1
    print(count)

isAllPrime(numbers)