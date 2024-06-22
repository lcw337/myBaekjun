numOfCal = int(input())

def calPoint(numOfCal):
    edge = 2
    for i in range(numOfCal):
        edge = edge + (edge-1)  #변 따로
    return edge**2  #제곱 따로

print(calPoint(numOfCal))




