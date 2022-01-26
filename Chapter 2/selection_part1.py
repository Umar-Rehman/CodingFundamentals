# Part 1

def check_age(age):
    while type(age) != int:
        try:
            age = int(age)
        except:
            age = input("Please enter your age as an integer value: ")
    if age >= 18:
        print("You are in category A\n")
    elif age >= 16:
        print("You are in category B\n")
    else:
        print("You are in category C\n")

check_age(input("Enter age: "))
