# Part 2 - Factorial 

def factorial(num1):
    while type(num1) != int:
        try:
            num1 = int(num1)
        except:
            num1 = input("Please enter an integer value: ")
    out = 1
    while num1 > 1:
        out = out*(num1)
        num1-=1
    print(out)
    return out
    
# To try the function yourself, uncomment the following lines:
# factorial(input("Enter an integer: "))