import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ExamGrade2

def test_calculate_exam_grade():
    assert ExamGrade2.calculate_exam_grade(1, 100) == "Level: 1\nGrade: Distinction"

def test_calculate_exam_grade():
    assert ExamGrade2.calculate_exam_grade(1, 65) == "Level: 1\nGrade: Merit"

def test_calculate_exam_grade():
    assert ExamGrade2.calculate_exam_grade(1, 55) == "Level: 1\nGrade: Pass"

def test_calculate_exam_grade():
    assert ExamGrade2.calculate_exam_grade(1, 45) == "Level: 1\nGrade: Fail"

def test_calculate_exam_grade():
    assert ExamGrade2.calculate_exam_grade(2, 100) == "Level: 2\nGrade: Distinction"

def test_calculate_exam_grade():
    assert ExamGrade2.calculate_exam_grade(2, 55) == "Level: 2\nGrade: Merit"

def test_calculate_exam_grade():
    assert ExamGrade2.calculate_exam_grade(2, 45) == "Level: 2\nGrade: Pass"

def test_calculate_exam_grade():
    assert ExamGrade2.calculate_exam_grade(2, 35) == "Level: 2\nGrade: Fail"