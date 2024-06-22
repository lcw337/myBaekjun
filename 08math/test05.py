a, b, v = map(int, input().split())
height = 0
count = 0
while True:
    height += a
    if height >= v:
        count += 1
        break
    height -= b
    count += 1

print(count)