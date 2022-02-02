from src import list_of_squares

def test_list_of_squares1():
    assert list_of_squares.list_of_squares(1) == {1: 1}

def test_list_of_squares2():
    assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}

def test_list_of_squares3():
    assert list_of_squares.list_of_squares(-1) == {}

def test_list_of_squares4():
    assert list_of_squares.list_of_squares(0) == {}