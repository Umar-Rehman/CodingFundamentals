import math


class Pythagoras:
    def __init__(self, num1, num2):
        self.first = num1
        self.second = num2

    def find_Side(self):
        a = math.sqrt(abs(self.first**2 - self.second**2))
        return a

    def find_Hyp(self):
        c = math.sqrt(self.first**2 + self.second**2)
        return c

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

def use_pythagoras():
    do = True
    while do:
        option = input("Pythagoras' Calculator:\n\n"+
        "      #       \n      ###     \n   A  #####   C\n      ####### \n      #########\n          B\n\n"+
        "1. Find the length of A given B and C \n" + 
        "2. Find the length of B given A and C\n3. Find the length of C given A and B\n" +
        "4. Exit\n")
        while type(option) != int:
            try:
                option = int(option)
                if int(option) < 1 or int(option) > 4:
                    raise Exception
                else:
                    continue
            except:
                option = input("Please enter an option between 1-4: ")

        if option == 1 or option == 2:
            num1, num2 = get_values()
            newp = Pythagoras(num1, num2)
            ans = newp.find_Side()
            print(f"\n{ans}\n\n")

        elif option == 3:
            num1, num2 = get_values()
            newp = Pythagoras(num1, num2)
            ans = newp.find_Hyp()
            print(f"\n{ans}\n\n")

        else:
            do = False

use_pythagoras()