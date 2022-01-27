# Part 1

def check_age(age):
    while type(age) != int:
        try:
            age = int(age)
        except:
            age = input("Please enter your age as an integer value: ")
    if age >= 18:
        print("You are in category A\n")
        return("A")
    elif age >= 16:
        print("You are in category B\n")
        return("B")
    else:
        print("You are in category C\n")
        return("C")

check_age(input("Enter age: "))
