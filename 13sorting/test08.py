numOfLocation = int(input())

locations = []

for _ in range(numOfLocation):
    locations.append(list(map(int, input().split())))

locations.sort(key=lambda arr: (arr[1], arr[0]))

for location in locations:
    print(location[0], location[1])