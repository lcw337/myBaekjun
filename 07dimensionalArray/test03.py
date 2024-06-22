matrix = []
for _ in range(5):
    matrix.append(input())


def printVertical(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(cols):    #느린거
        for j in range(rows):   #빠른거
            try:
                print(matrix[j][i], end="")     #층은 빨리변함
            except: #오류나도 죽지마
                pass


printVertical(matrix)