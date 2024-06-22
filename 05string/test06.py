myString = input()
# checkAlphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets = list(alphabets)

checkIndexes = []

for alphabet in alphabets:
    checkIndexes.append(myString.find(alphabet))

for checkIndex in checkIndexes:
    print(checkIndex, end = " ")