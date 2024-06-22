def printSign():
    if a>b:
        print(">")
    elif a<b:
        print("<")
    else:
        print("==")

a,b=map(int,input().split())
printSign()