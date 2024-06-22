def isLeap(year):
    if year%4==0 and year%100!=0:
        return 1
    elif year%400==0:
        return 1
    else:
        return 0
def printResult(year):
    if isLeap(year):
        print("1")
    else:
        print("0")
year=int(input())
printResult(year)

