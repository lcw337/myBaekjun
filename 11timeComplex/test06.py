n = int(input())
new_n = n - 2
def sumUnder(n):
    return int(n * (n+1) * 1/2)

result = 0
while new_n > 0:
    result += sumUnder(new_n)
    new_n -= 1

print(int(result))
print(3)