# Anagram Detector

def detect_anagram():
    first = list(input())
    second = list(input())
    if sorted(first) == sorted(second):
        print("Anagram detected.")
    else:
        print("Anagram NOT detected.")
    
detect_anagram()