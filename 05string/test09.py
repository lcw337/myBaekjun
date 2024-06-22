num1, num2 = map(list, input().split())

num1.reverse()
num1 = int(''.join(num1))

num2.reverse()
num2 = int(''.join(num2))

print(max(num1, num2))
