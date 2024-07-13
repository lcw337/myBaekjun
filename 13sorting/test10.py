N = int(input())
informs = []

for _ in range(N):
    age, name = input().split()
    informs.append([int(age), name])

informs.sort(key=lambda a: a[0])

for inform in informs:
    print(inform[0], inform[1])