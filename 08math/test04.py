def findPosition(): #타겟위치찾는로직
    group = 1
    count = 1   #첫째라인껀 초기화 하면서 끝내
    while target > count:
        group += 1
        count += group
    groupPosition = target - count + group    #그그룹 주변가서 찾기
    return group, groupPosition

def makeFrac(group, groupPosition):
    if group % 2 == 0:
        sum = group + 1 #합이 그룹+1로 일정해서
        topnum = groupPosition  #그대로
        bottomnum = sum - groupPosition #보수느낌
    else:
        sum = group + 1
        topnum = sum - groupPosition
        bottomnum = groupPosition
    return str(f"{topnum}/{bottomnum}")

target = int(input())
group, groupPosition = findPosition()
result = makeFrac(group, groupPosition)
print(result)