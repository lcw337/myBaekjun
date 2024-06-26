min_input = int(input())
max_input = int(input())
prime_nums = []

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for num in range(min_input, max_input+1):
    if isPrime(num):
        prime_nums.append(num)

if prime_nums:
    print(sum(prime_nums))
    print(min(prime_nums))
else:
    print("-1")