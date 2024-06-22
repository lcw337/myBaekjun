lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break


for line in lines:
    print(line)
#ctrl + d 가 입력종료 에러발생시킴