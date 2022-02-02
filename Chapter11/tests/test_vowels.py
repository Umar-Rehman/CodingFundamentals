from src import vowels

def test_vowels1():
    assert vowels.vowels("peanut") == 3

def test_vowels2():
    assert vowels.vowels("butter") == 2

def test_vowels3():
    assert vowels.vowels("jelly") == 1

def test_vowels4():
    assert vowels.vowels("TIME") == 2