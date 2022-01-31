# Palindrome

def palindrome():
    word = list(input())
    word2 = list(reversed(word))
    if word == word2:
        print("Yes")
    else:
        print("No")