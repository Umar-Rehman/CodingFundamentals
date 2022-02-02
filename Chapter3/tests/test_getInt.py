from src import getInt, base

def test_getInt1():
    base.set_keyboard_input(["1"])
    assert getInt.getInt() == "Correct"

def test_getInt2():
    base.set_keyboard_input(["0", "0", "101"])
    assert getInt.getInt() == None

def test_getInt3():
    base.set_keyboard_input(["0", "101", "50"])
    assert getInt.getInt() == "Correct"

def test_getInt4():
    base.set_keyboard_input(["one", "two", "three", "1"])
    assert getInt.getInt() == "Correct"
