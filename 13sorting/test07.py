numOfLocation = int(input())

locations = []

for _ in range(numOfLocation):
    locations.append(list(map(int, input().split())))

locations.sort()

for location in locations:
    print(location[0], end=" ")
    print(location[1])