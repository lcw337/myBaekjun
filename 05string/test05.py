numOfTry = int(input())
sum = 0
numString = input()
nums = []
for i in range(len(numString)):
    nums.append(numString[i])
for num in nums:
    sum += int(num)

print(sum)