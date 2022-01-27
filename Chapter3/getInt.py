# Part 4 – Input an integer between two limits

def getInt(min=1, max=100):
    attempts = 1
    while attempts <=3:
        user_value = input(f"Enter an integer between {min}-{max}: ")
        while type(user_value) != int:
            try:
                user_value = int(user_value)
            except:
                user_value = input(f"Enter an integer between {min}-{max}: ")
        if user_value < min or user_value > max:
            if attempts == 3:
                print(None)
            attempts+=1
        else:
            print(f"You entered {user_value}!")
            break

getInt()