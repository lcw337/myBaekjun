def printGugudan():
    global n
    for i in range(1, 10):
        print(n, "*", i, "=", n*i)
n = int(input())
printGugudan()