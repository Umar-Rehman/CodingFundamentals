# Part 5 - Count vowels 

def count_vowels(word):
    vowels = ("a", "e", "i", "o", "u")
    count=0
    for i in word.lower():
        if i in vowels:
            count+=1
    print(f"I count {count} vowel(s).")
    return count

# To try the function yourself, uncomment the following lines:
# count_vowels(input("Enter a word: ").lower())