def selectBaseNum():
    global first, second, third
    if first == second == third:
        return first
    elif first == second or second == third or first == third:
        if first == second:
            return first
        elif second == third:
            return second
        else:
            return  third
    else:
        if first > second and first >third:
            return first
        elif second > first and second >third:
            return second
        else:
            return third

def calculateReward():
    global first, second, third
    if first == second == third:
        reward = 10000 + selectBaseNum() * 1000
    elif first == second or second == third or first == third:
        reward = 1000 + selectBaseNum() * 100
    else:
        reward = selectBaseNum() * 100

    return reward
def printReward():
    print(calculateReward())

first, second, third = map(int, input().split())
printReward()