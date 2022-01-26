# Part 2
# Excercise 2

def calculate_grade():
    mark = input("Enter exam mark from 1-100: ")
    while type(mark) != int:
        try:
            mark = int(mark)
            if mark < 1 or mark > 100:
                raise Exception
            else:
                continue
        except:
            mark = input("Please enter an integer value between 1-100: ")
    
    if mark > 70:
        print("Grade: Distinction")
    elif mark > 60:
        print("Grade: Merit")
    elif mark > 49:
        print("Grade: Pass")
    else:
        print("Grade: Fail")

calculate_grade()