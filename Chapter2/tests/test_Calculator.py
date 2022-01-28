import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Calculator

def test_add():
    newCalc = Calculator.Calculator(5, 9)
    ans = newCalc.add()
    assert ans == 14

def test_subtract():
    newCalc = Calculator.Calculator(5, 9)
    ans = newCalc.subtract()
    assert ans == -4

def test_multiply():
    newCalc = Calculator.Calculator(5, 9)
    ans = newCalc.multiply()
    assert ans == 45

def test_divide():
    newCalc = Calculator.Calculator(45, 9)
    ans = newCalc.divide()
    assert ans == 5