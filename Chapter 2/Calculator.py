# Part 2
# Excercise 1

class Calculator:

    def __init__(self, num1, num2):
        self.first = num1
        self.second = num2

    def add(self):
        x = self.first + self.second
        return x

    def subtract(self):
        y = self.first - self.second
        return y

    def multiply(self):
        z = self.first * self.second 
        return z

    def divide(self):
        a = self.first / self.second
        return a
    

def get_values():
    num1 = input("Enter first number: ")
    while type(num1) != float:
        try:
            num1 = float(num1)
        except:
            num1 = input("Please enter an integer/float value: ")

    num2 = input("Enter second number: ")
    while type(num2) != float:
        try:
            num2 = float(num2)
        except:
            num2 = input("Please enter an integer/float value: ")

    return num1, num2

def calculate():
    do = True
    while do:
        option = input("Select an operation:\n1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)\n5. Square (^2)\n6. Exit\n")
        while type(option) != int:
            try:
                option = int(option)
                if int(option) < 1 or int(option) > 6:
                    raise Exception
                else:
                    continue
            except:
                option = input("Please enter an option between 1-6: ")

        if option == 1:
            num1, num2 = get_values()
            newc = Calculator(num1, num2)
            ans = newc.add()
            print(ans)
        elif option == 2:
            num1, num2 = get_values()
            newc = Calculator(num1, num2)
            ans = newc.subtract()
            print(ans)
        elif option == 3:
            num1, num2 = get_values()
            newc = Calculator(num1, num2)
            ans = newc.multiply()
            print(ans)
        elif option == 4:
            num1, num2 = get_values()
            newc = Calculator(num1, num2)
            ans = newc.divide()
            print(ans)
        elif option == 5:
            num1 = input("Enter first number: ")
            while type(num1) != float:
                try:
                    num1 = float(num1)
                except:
                    num1 = input("Please enter an integer/float value: ")
            ans = num1*num1
            print(ans)
        else:
            do = False

    
calculate()