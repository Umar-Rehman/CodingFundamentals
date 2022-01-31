# 3. Multiplication table 

def table(num):
    while type(num) != int:
        try:
            num = int(num)
        except:
            num = input("Please enter an integer value: ")

    for i in range(1,11):
        print(f"{i}x{num}={i*num}")

table(input("Enter an integer: "))