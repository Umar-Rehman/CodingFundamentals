from src import tax

def test_getIncomeTax1():
    assert tax.getIncomeTax(0) == (0.0, 0.0, 0.0)

def test_getIncomeTax2():
    assert tax.getIncomeTax(1000) == (0.2, 200.0, 800.0)

def test_getIncomeTax3():
    assert tax.getIncomeTax(40000) == (0.4, 16000.0, 24000.0)

def test_getIncomeTax4():
    assert tax.getIncomeTax(500000) == (0.45, 225000.0, 275000.0)