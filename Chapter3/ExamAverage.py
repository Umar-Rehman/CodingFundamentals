# Part 6 - Exam average

def get_marks(num):
    marks = []
    for i in range(0,num):
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
        marks.append(mark)
    return marks

def find_average(num=3):
    marks = get_marks(num)
    average = round(sum(marks) / len(marks))
    if average >= 65:
        result = "Pass"
    else:
        result = "Fail"
    
    print(f"Average: {average}\nResult: {result}")
    return average, result

# To try the function yourself, uncomment the following lines:
# find_average()