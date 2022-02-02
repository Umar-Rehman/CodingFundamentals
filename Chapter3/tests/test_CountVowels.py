from src import CountVowels

def test_count_vowels1():
    assert CountVowels.count_vowels("peanut") == 3

def test_count_vowels2():
    assert CountVowels.count_vowels("butter") == 2

def test_count_vowels3():
    assert CountVowels.count_vowels("jelly") == 1

def test_count_vowels4():
    assert CountVowels.count_vowels("TIME") == 2
