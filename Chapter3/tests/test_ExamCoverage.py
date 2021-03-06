import pytest
from src import ExamAverage, base

## Testing get_marks function
@pytest.fixture
def get_marks_num_1():
    return 1

@pytest.fixture
def get_marks_num_2():
    return 4

@pytest.fixture
def get_marks_num_3():
    return 6

def test_get_marks1(get_marks_num_1):
    base.set_keyboard_input(["1"])
    assert ExamAverage.get_marks(get_marks_num_1) == [1]

def test_get_marks2(get_marks_num_2):
    base.set_keyboard_input(["1", "1", "1", "1"])
    assert ExamAverage.get_marks(get_marks_num_2) == [1, 1, 1, 1]

def test_get_marks3(get_marks_num_3):
    base.set_keyboard_input(["1", "1", "1", "1", "1", "1"])
    assert ExamAverage.get_marks(get_marks_num_3) == [1, 1, 1, 1, 1, 1]

## Testing find_average function
def test_find_average1():
    base.set_keyboard_input(["1", "1", "1"])
    assert ExamAverage.find_average() == (1, "Fail")

def test_find_average2():
    base.set_keyboard_input(["0", "101", "1", "1", "1"])
    assert ExamAverage.find_average() == (1, "Fail")

def test_find_average3():
    base.set_keyboard_input(["50", "70", "80"])
    assert ExamAverage.find_average() == (67, "Pass")