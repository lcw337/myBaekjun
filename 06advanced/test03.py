sentens = input()
def ispalindrome(sentens):
    temp = sentens
    sentens = list(sentens)
    palindrome = []
    for i in range(len(sentens)):
        palindrome.append(sentens.pop())
    if list(temp) == palindrome:
        return 1
    else:
        return 0
print(ispalindrome(sentens))