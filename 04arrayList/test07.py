studentsNums = []
for _ in range(28):
    studentsNums.append(int(input()))

absentStudents = []

for i in range(1, 31):
    if i not in studentsNums:
        absentStudents.append(i)

absentStudents.sort()
for i in range(len(absentStudents)):
    print(absentStudents[i])