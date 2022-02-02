from src import selection_part1

def test_check_age1():
    assert selection_part1.check_age(20) == "A"

def test_check_age2():
    assert selection_part1.check_age(17) == "B"

def test_check_age3():
    assert selection_part1.check_age(15) == "C"