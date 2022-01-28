import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Squares_forloop

def test_square():
    assert Squares_forloop.square() == (45, 2025)