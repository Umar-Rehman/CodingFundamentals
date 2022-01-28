import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Factorial

def test_factorial():
    assert Factorial.factorial(0) == 1

def test_factorial():
    assert Factorial.factorial(1) == 1

def test_factorial():
    assert Factorial.factorial(2) == 2

def test_factorial():
    assert Factorial.factorial(5) == 120

def test_factorial():
    assert Factorial.factorial(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000