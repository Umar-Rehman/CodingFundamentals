from src import Factorial

def test_factorial1():
    assert Factorial.factorial(0) == 1

def test_factorial2():
    assert Factorial.factorial(1) == 1

def test_factorial3():
    assert Factorial.factorial(2) == 2

def test_factorial4():
    assert Factorial.factorial(5) == 120

def test_factorial5():
    assert Factorial.factorial(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000