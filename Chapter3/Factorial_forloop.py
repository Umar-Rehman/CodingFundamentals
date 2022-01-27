# Part 2 - Factorial 

# 2. Inputs an integer.
# 3. Display the number's factorial.
# Tip: the factorial of a number is that number multiplied by all the preceding 
# numbers.
# 4
# The factorial of 5 is = 5 x 4 x 3 x 2 x 1 = 120 
# Or, if you like = 1 x 2 x 3 x 4 x 5
# 4. Save and run

def factorial():
    num1 = input("Enter an integer: ")
    while type(num1) != int:
        try:
            num1 = int(num1)
        except:
            num1 = input("Please enter an integer value: ")
    out = 1
    for i in range(1, num1+1):
        out = out*i
    print(out)

factorial()