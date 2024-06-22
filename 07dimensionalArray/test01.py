row, col = map(int, input().split())
matrix1 = []
matrix2 = []


def getmatrix(matrix, row, col):
    for i in range(row):
        matrix.append(list(map(int, input().split())))


getmatrix(matrix1, row, col)
getmatrix(matrix2, row, col)


def summatrix(matrix1, matrix2, row, col):
    for i in range(row):
        for j in range(col):
            print(matrix1[i][j] + matrix2[i][j], end=" ")
        print()

summatrix(matrix1, matrix2, row, col)