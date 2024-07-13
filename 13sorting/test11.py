N = int(input())
locations = list(map(int, input().split()))

indexes = sorted(list(set(locations)))
for location in locations:
    print(indexes.index(location), end=" ")

