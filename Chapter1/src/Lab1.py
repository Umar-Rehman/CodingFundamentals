# Part 1 - Display Hello World!
def greet():
    message = "Hello, World!"
    print(message, "\n")
    return message

# Part 2 - Display a message using variables
def stock_message():
    name = "Umar"
    age = 24
    message = f"{name} is {age} years old"
    print(message, "\n")
    return message

# Part 2.5 – Get user input
def custom_message(name, age):
    while type(age) != int:
        try:
            age = int(age)
            message = f"{name} is {age} years old!"
            print(message, "\n")
            return message
        except:
            age = input("Please enter your age as an integer value: ")

# Part 3
def calculate_area_perim(length, width):
    while type(length) != int:
        try:
            length = int(length)
        except:
            length = input("Please enter an integer length: ")
    while type(width) != int:
        try:
            width = int(width)
        except:
            width = input("Please enter an integer width: ")
    area = length*width
    perim = 2*(length + width)
    print(f"Area: {area}\nPerimeter: {perim}")
    return area, perim

# To try the functions yourself, uncomment the following lines:
# greet()
# stock_message()
# custom_message(input("Enter name: "), input("Enter age: "))
# calculate_area_perim(input("Enter length: "), input("Enter width: "))