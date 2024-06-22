nums = []
count = 0

for _ in range(10):
    nums.append(int(input()))

modResults = []
for i in range(10):
    modResults.append(nums[i] % 42)

for i in range(10):
    if modResults[i] not in modResults[:i]:
        count += 1

print(count)