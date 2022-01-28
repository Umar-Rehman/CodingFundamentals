import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tax

def test_getIncomeTax():
    assert tax.getIncomeTax(0) == (0.0, 0.0, 0.0)

def test_getIncomeTax():
    assert tax.getIncomeTax(1000) == (0.2, 200.0, 800.0)

def test_getIncomeTax():
    assert tax.getIncomeTax(40000) == (0.4, 16000.0, 24000.0)

def test_getIncomeTax():
    assert tax.getIncomeTax(500000) == (0.45, 225000.0, 275000.0)