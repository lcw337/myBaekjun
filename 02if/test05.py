def realTime():
    global H,M
    M+=60
    H-=1
    if H<0:
        H+=24

def setBackTo45():
    global H, M
    M-=45
    if M<0:
        realTime()

def printBackTo45():
    global H, M     #메모리가 할당되는게아님
    setBackTo45()
    print(H,M)

H, M = map(int, input().split())
printBackTo45()