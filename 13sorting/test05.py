import sys

numOfInputs = int(input())

nums = []
for _ in range(numOfInputs):
    nums.append(int(sys.stdin.readline()))
    #버퍼없이 즉시 입력받아서 입력량 많을수록 속도유리

nums.sort()
for num in nums:
    print(num)