dots = []

for _ in range(3):
    dot = list(map(int, input().split()))
    dots.append(dot)

xs = []
ys = []

for dot in dots:
    xs.append(dot[0])
    ys.append(dot[1])

for x in xs:
    if xs.count(x) == 1:
        x4 = x
        print(x4, end=" ")
for y in ys:
    if ys.count(y) == 1:
        y4 = y
        print(y4)


