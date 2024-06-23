inputs = []
while True:
    nums = list(map(int, input().split()))
    if nums == [0, 0]:
        break
    inputs.append(nums)

for input_ in inputs:
    if input_[1] % input_[0] == 0:
        print("factor")
    elif input_[0] % input_[1] == 0:
        print("multiple")
    else:
        print("neither")
