# Part 2 - Factorial 

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