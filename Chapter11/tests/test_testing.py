from src import testing

def test_count_string():
    assert testing.count("Hello, World!", "l") == 3

def test_count_integers():
    assert testing.count([1,2,3,3,4,5,6,6], 3) == 2
