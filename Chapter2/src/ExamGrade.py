# Part 2
# Excercise 2

def calculate_grade(mark):
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
        return("Grade: Distinction")
    elif mark > 60:
        print("Grade: Merit")
        return("Grade: Merit")
    elif mark > 49:
        print("Grade: Pass")
        return("Grade: Pass")
    else:
        print("Grade: Fail")
        return("Grade: Fail")

# To try the function yourself, uncomment the following line:
# calculate_grade(input("Enter exam mark from 1-100: "))