# Who's in the building

from numpy import who


def who_in():
    out = False
    register = []
    while out == False:
    
        state = input("Enter in/out (or quit to stop the program): ").lower()
        if state == "quit":
            out = True
        elif state == "in" or state == "out":
            who = input("Enter name: ").lower()

            if state == "in":
                if who in register:
                    print(f"{who} is already in the building.")
                else:
                    register.append(who)
            elif state == "out":
                try:
                    register.remove(who)
                except:
                    print(f"{who} is not in the building.")
            print(f"People in the building: {register}")
        else:
            print("Please enter either 'in', 'out' or 'quit'.")

who_in()