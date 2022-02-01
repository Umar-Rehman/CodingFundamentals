# Fizz Buzz

def fizzBuzz(num):
    while type(num) != int:
        try:
            num = int(num)
        except:
            num = input("Please enter an integer value: ")
    li = []
    for i in range(1, num+1):
        if i%3 == 0 and i%5 ==0:
            li.append("FIZZ BUZZ")
            continue
        if i%3 == 0:
            li.append("FIZZ")
            continue
        if i%5 == 0:
            li.append("BUZZ")
            continue
        else:
            li.append(i)
    
    print(li)

fizzBuzz(input("Enter length of list: "))