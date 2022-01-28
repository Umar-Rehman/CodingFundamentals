import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import CountVowels

def test_count_vowels():
    assert CountVowels.count_vowels("peanut") == 3

def test_count_vowels():
    assert CountVowels.count_vowels("butter") == 2

def test_count_vowels():
    assert CountVowels.count_vowels("jelly") == 1

def test_count_vowels():
    assert CountVowels.count_vowels("TIME") == 2
