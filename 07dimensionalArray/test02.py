matrix = []
for i in range(9):
    matrix.append(list(map(int, input().split())))


def findMax(m):
    max = 0
    x = 0
    y = 0
    for i in range(9):
        for j in range(9):
            if m[i][j] > max:
                max = m[i][j]
                x = i
                y = j

    return x, y, max


x, y, max = findMax(matrix)
print(max, x + 1, y + 1)