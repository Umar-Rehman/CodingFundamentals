# Estimated time of arrival 
## Needs changes for large times, to show an eta for the day at which you will arrive

from datetime import datetime

def get_values():
    distance = input("Enter distance (in miles): ")
    while type(distance) != float:
            try:
                distance = float(distance)
            except:
                distance = input("Please enter an integer/float value for distance: ")
    speed = input("Enter speed (in miles per hour): ")
    while type(speed) != float:
            try:
                speed = float(speed)
            except:
                speed = input("Please enter an integer/float value for distance: ")
    return distance, speed

def eta():
    distance, speed = get_values()
    t = round((distance/speed), 2)
    hours = int(t)
    mins = round((t%1)*60)
    now = datetime.now().strftime("%H:%M")
    li = list(map(int, now.split(":")))
    li[0]+=hours
    li[1]+=mins

    if li[1] > 59:
        li[0]+= li[1]//60
        li[1] = li[1]%60

    print(f"ETA: {li[0]}:{li[1]}")

eta()