import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Squares

def test_getInt():
    assert Squares.while_square() == 45