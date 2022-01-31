# Train message display 

def train_message(li):
    if len(li) == 1:
        print(f"This train is for {li[0]}, final stop.")
    elif len(li) == 2:
        print(f"This train is for {li[1]}, calling at {li[0]}.")
    else:
        last = li[len(li)-1]
        li.pop()
        penultimate = li[len(li)-1]
        li.pop()
        print(f"This train is for {last}, calling at {', '.join(li)} and {penultimate}.")
    
train_message(["Rochdale", "Halifax", "Bradford", "Pudsey", "Leeds"])