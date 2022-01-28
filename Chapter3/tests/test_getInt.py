import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import getInt, base

def test_getInt():
    base.set_keyboard_input(["1"])
    assert getInt.getInt() == "Correct"

def test_getInt():
    base.set_keyboard_input(["0", "0", "101"])
    assert getInt.getInt() == None

def test_getInt():
    base.set_keyboard_input(["0", "101", "50"])
    assert getInt.getInt() == "Correct"

def test_getInt():
    base.set_keyboard_input(["one", "two", "three", "1"])
    assert getInt.getInt() == "Correct"
