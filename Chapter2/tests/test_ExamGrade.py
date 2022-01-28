import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ExamGrade

def test_calculate_grade():
    assert ExamGrade.calculate_grade(100) == "Grade: Distinction"

def test_calculate_grade():
    assert ExamGrade.calculate_grade(61) == "Grade: Merit"

def test_calculate_grade():
    assert ExamGrade.calculate_grade(50) == "Grade: Pass"

def test_calculate_grade():
    assert ExamGrade.calculate_grade(20) == "Grade: Fail"
