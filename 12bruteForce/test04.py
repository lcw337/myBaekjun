#입력 -> 8*8주어질때 판단하는로직 -> 8*8로자르는로직
userRow, userCol = map(int, input().split())

userMap = []
for _ in range(userRow):
    userMap.append(list(input()))
def bestRepaint(board):
    pattern1 = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
    ]

    pattern2 = [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
    ]
    repaint1 = 0
    repaint2 = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] != pattern1[x][y]:
                repaint1 += 1
            if board[x][y] != pattern2[x][y]:
                repaint2 += 1
    return min(repaint1, repaint2)
    #이제 패턴2개는 고려안해도됌

allMapSol = float("inf")
for startRow in range(userRow-7):
    for startCol in range(userCol-7):
        newMap = []
        for x in range(8):
            extendedRow = []
            for y in range(8):
                extendedRow.append(userMap[startRow+x][startCol+y])
            newMap.append(extendedRow)
        oneMapSol = bestRepaint(newMap)
        allMapSol = min(allMapSol, oneMapSol)

print(allMapSol)
