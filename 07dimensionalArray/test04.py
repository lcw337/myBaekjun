# 빈 행렬을 생성
matrix = []
# 5개의 줄을 입력받아 행렬에 추가
for _ in range(5):
    matrix.append(input())

# 수직으로 행렬을 출력하는 함수
def printVertical(matrix):
    # 행의 개수와 첫 행의 열 개수를 계산
    rows = len(matrix)
    cols = max(len(row) for row in matrix)

    # 열을 반복
    for c in range(cols):
        # 행을 반복하며 수직으로 출력
        for r in range(rows):
            if c < len(matrix[r]):  # 사각형안만들어지면 출력하지마
                print(matrix[r][c], end="")

# 수직 출력 함수 호출
printVertical(matrix)
