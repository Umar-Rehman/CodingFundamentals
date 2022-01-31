# Sleeps until next birthday

import datetime

def find_sleeps():
    good_input = False
    dob = input("Enter D.O.B (DD:MM:YYYY): ")
    while good_input == False:
        try:
            dob_list = list(map(int,dob.split(":")))

            today = datetime.datetime.today()
            dob = datetime.datetime(2022, dob_list[1], dob_list[0])

            duration = abs(today - dob)
            age = today.year - dob_list[2]
            print(f"In {duration.days} sleeps, you will be {age} years old")
            good_input = True
        except:
            dob = input("Enter D.O.B (in format DD:HH:MM): ")

find_sleeps()