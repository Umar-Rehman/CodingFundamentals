import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import inbuiltFunctions

def test_analyze_csv_list():
    data = "1,2,3,4,5"
    assert inbuiltFunctions.analyze_csv_list(data) == (1, 5, 3, 3, 3)

def test_analyze_csv_list():
    data = "2,4,6,8,10"
    assert inbuiltFunctions.analyze_csv_list(data) == (2, 10, 6, 6, 6)

def test_analyze_csv_list():
    data = "123,43,21,92,512"
    assert inbuiltFunctions.analyze_csv_list(data) == (21, 512, 158.2, 158.2, 92)
