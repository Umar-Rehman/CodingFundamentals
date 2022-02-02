from src import ExamGrade2

def test_calculate_exam_grade1():
    assert ExamGrade2.calculate_exam_grade(1, 100) == "Level: 1\nGrade: Distinction"

def test_calculate_exam_grade2():
    assert ExamGrade2.calculate_exam_grade(1, 65) == "Level: 1\nGrade: Merit"

def test_calculate_exam_grade3():
    assert ExamGrade2.calculate_exam_grade(1, 55) == "Level: 1\nGrade: Pass"

def test_calculate_exam_grade4():
    assert ExamGrade2.calculate_exam_grade(1, 45) == "Level: 1\nGrade: Fail"

def test_calculate_exam_grade5():
    assert ExamGrade2.calculate_exam_grade(2, 100) == "Level: 2\nGrade: Distinction"

def test_calculate_exam_grade6():
    assert ExamGrade2.calculate_exam_grade(2, 55) == "Level: 2\nGrade: Merit"

def test_calculate_exam_grade7():
    assert ExamGrade2.calculate_exam_grade(2, 45) == "Level: 2\nGrade: Pass"

def test_calculate_exam_grade8():
    assert ExamGrade2.calculate_exam_grade(2, 35) == "Level: 2\nGrade: Fail"