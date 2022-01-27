# Part 2 – Count vowels

def count_vowels():
    vowels = ["a", "e", "i", "o", "u"]
    word = input("Enter a word: ").lower()
    count=0
    for i in word:
        if i in vowels:
            count+=1
    print(f"I count {count} vowel(s).")

count_vowels()