from src import ExamGrade

def test_calculate_grade1():
    assert ExamGrade.calculate_grade(100) == "Grade: Distinction"

def test_calculate_grade2():
    assert ExamGrade.calculate_grade(61) == "Grade: Merit"

def test_calculate_grade3():
    assert ExamGrade.calculate_grade(50) == "Grade: Pass"

def test_calculate_grade4():
    assert ExamGrade.calculate_grade(20) == "Grade: Fail"
