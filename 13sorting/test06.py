nums = list(map(int, input()))
nums.sort()
for i in range(1, len(nums)+1):
    print(nums[-i], end="")