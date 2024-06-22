word = input()
word = word.upper()
wordList = list(word)
wordSet = set(wordList)
wordDict = {}
for w in wordSet:
    wordDict[w] = wordList.count(w) #zaaabbxxx -> {'Z': 1, 'A': 3, 'B': 2, 'X': 3}

maxValue = max(wordDict.values())
#.values()는 딕셔너리의 값들만 모아서 리스트로반환
if list(wordDict.values()).count(maxValue) > 1: #최댓값의 객수 (1323일때 3의갯수)
    print("?")
else:
    for key, value in wordDict.items(): #튜플로 반환
        if value == maxValue:
            print(key)
