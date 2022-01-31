# Summing numbers 1 - 100, but skipping every 4th number 

def sum_to_100():
    total = 0
    for i in range (1,101):
        if i%4 == 0:
            continue
        total+=i
    print(total)

sum_to_100()
