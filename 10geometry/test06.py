angles = []
for _ in range(3):
    angles.append(int(input()))

def whatTri(angles):
    if max(angles) == min(angles):
        print("Equilateral")
    elif angles[0] != angles[1] and angles[1] != angles[2] and angles[0] != angles[2]:
        print("Scalene")
    else:
        print("Isosceles")

if sum(angles) == 180:
    whatTri(angles)
else:
    print("Error")