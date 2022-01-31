# Biggest number 

def biggest_num():
    nums = []
    for i in range(0,5):
        num = input("Enter a number: ")
        while type(num) != int:
            try:
                num = int(num)
            except:
                num = input("Please enter an integer value: ")
        nums.append(num)
    print(max(list(map(int,nums))))

def biggest_num2():
    big = None
    for i in range(0, 5):
        num = input("Enter a number: ")
        while type(num) != int:
            try:
                num = int(num)
            except:
                num = input("Please enter an integer value: ")
        
        if big == None or num > big:
            big = num

    print(f"The biggest number entered was {big}")

# biggest_num()
# biggest_num2()