# Excercise 3

def calculate_exam_grade(level, mark):

    while type(level) != int:
        try:
            level = int(level)
            if level < 1 or level > 2:
                raise Exception
            else:
                continue
        except:
            level = input("Please enter a student level between 1-2: ")

    while type(mark) != int:
        try:
            mark = int(mark)
            if mark < 1 or mark > 100:
                raise Exception
            else:
                continue
        except:
            mark = input("Please enter an integer value between 1-100: ")
        
    if level == 1:
        if mark > 70:
            print(f"Level: {level}\nGrade: Distinction")
            return(f"Level: {level}\nGrade: Distinction")
        elif mark > 60:
            print(f"Level: {level}\nGrade: Merit")
            return(f"Level: {level}\nGrade: Merit")
        elif mark > 49:
            print(f"Level: {level}\nGrade: Pass")
            return(f"Level: {level}\nGrade: Pass")
        else:
            print(f"Level: {level}\nGrade: Fail")
            return(f"Level: {level}\nGrade: Fail")
    else:
        if mark > 65:
            print(f"Level: {level}\nGrade: Distinction")
            return(f"Level: {level}\nGrade: Distinction")
        elif mark > 50:
            print(f"Level: {level}\nGrade: Merit")
            return(f"Level: {level}\nGrade: Merit")
        elif mark > 39:
            print(f"Level: {level}\nGrade: Pass")
            return(f"Level: {level}\nGrade: Pass")
        else:
            print(f"Level: {level}\nGrade: Fail")
            return(f"Level: {level}\nGrade: Fail")

# To try the function yourself, uncomment the following line:
# calculate_exam_grade(input("Enter student level (1 or 2): "), input("Enter exam mark from 1-100: "))