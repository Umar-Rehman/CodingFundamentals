import os, sys, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import selection_part1

def test_check_age():
    assert selection_part1.check_age(20) == "A"

def test_check_age():
    assert selection_part1.check_age(17) == "B"

def test_check_age():
    assert selection_part1.check_age(15) == "C"