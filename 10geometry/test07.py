lines = []
while True:
    lines.append(list(map(int, input().split())))
    if lines[-1] == [0, 0, 0]:
        lines.pop()
        break

for line in lines:
    if max(line) < sum(line) - max(line):
        if line[0] == line[1] and line[1] == line[2]:
            print("Equilateral")
        elif line[0] != line[1] and line[1] != line[2] and line[2] != line[0]:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")
