numOfTry = int(input())

dots = []
for _ in range(numOfTry):
    dots.append(list(map(int, input().split())))

xs = []
ys = []
for dot in dots:
    xs.append(dot[0])
    ys.append(dot[1])

area = (max(xs)-min(xs)) * (max(ys)-min(ys))

print(area)