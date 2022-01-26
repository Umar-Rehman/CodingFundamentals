# Part 1 - Display Hello World!
def greet():
    message = "Hello, World!"
    print(message, "\n")
    return message

greet()

# Part 2 - Display a message using variables
def stock_message():
    name = "Umar"
    age = 24
    message = f"{name} is {age} years old"
    print(message, "\n")
    return message

stock_message()

# Part 2.5 – Get user input
def custom_message():
    name = input("Enter name: ")
    age = input("Enter age: ")
    while type(age) != int:
        try:
            age = int(age)
            message = f"{name} is {age} years old!"
            print(message, "\n")
            return message
        except:
            age = input("Please enter your age as an integer value: ")
    

custom_message()

# Part 3
def calculate_area_perim():
    length = input("Enter length: ")
    while type(length) != int:
        try:
            length = int(length)
        except:
            length = input("Please enter an integer length: ")
    width = input("Enter width: ")
    while type(width) != int:
        try:
            width = int(width)
        except:
            width = input("Please enter an integer width: ")
    area = length*width
    perim = 2*(length + width)
    print(f"Area: {area}\nPerimeter: {perim}")
    return area, perim

calculate_area_perim()