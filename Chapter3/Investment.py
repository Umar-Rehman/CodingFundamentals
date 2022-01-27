# Part 3 - Investment 

def get_values():
    initial = input("Enter initial investment: ")
    if initial.__contains__('£'):
        initial = initial.replace('£', '')

    while type(initial) != float:
        try:
            initial = float(initial)
        except:
            initial = input("Please enter an integer/float value for initial investment: ")

    target = input("Enter target value: ")
    if target.__contains__('£'):
        target = target.replace('£', '')

    while type(target) != float:
        try:
            target = float(target)
        except:
            target = input("Please enter an integer/float value for target value: ")
    
    rate = input("Enter interest rate p/a as a %: ")
    if rate.__contains__('%'):
        rate = rate.replace('%', '')

    while type(rate) != float:
        try:
            rate = float(rate)
        except:
            rate = input("Please enter an integer/float value for interest rate p/a as a %: ")

    return initial, target, rate

def investment():
    initial, target, rate = get_values()
    out = initial
    years = 0
    while out < target:
        out += out*(rate/100)
        years += 1

    print(f"It will take {years} to reach £{out.__round__(2)}.")

investment()
