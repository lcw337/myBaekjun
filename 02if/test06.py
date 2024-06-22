def realTime():
    global hour, minute
    minute -= 60
    hour += 1
    if hour >= 24:
        hour -= 24

def calculateEndTime():
    global hour, minute, requiredTime
    minute += requiredTime
    while minute >= 60:
        realTime()
def printEndTime():
    global hour, minute
    calculateEndTime()
    print(hour, minute)

hour, minute = map(int, input().split())
requiredTime = int(input())
printEndTime()