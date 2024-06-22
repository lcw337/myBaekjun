a, b, v = map(int, input().split())

targetExceptLast = v - a    #막타 직전
onlyOnedayGrow = a - b  #순수 하루성장

if targetExceptLast % onlyOnedayGrow == 0:
    days = targetExceptLast // onlyOnedayGrow
else:
    days = targetExceptLast // onlyOnedayGrow + 1   #몫계산이니 버림되서 다시올림함(0.25일 걸린건도 1일 처리)

count = days + 1

print(count)
