import os, sys, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Lab1

def test_greet():
    assert Lab1.greet() == "Hello, World!"

def test_stock_message():
    assert Lab1.stock_message() == "Umar is 24 years old"

def test_custom_message():
    assert Lab1.custom_message("Bob", "30") == "Bob is 30 years old!"

def test_calculate_area_perim():
    assert Lab1.calculate_area_perim(5, 3) == (15, 16)