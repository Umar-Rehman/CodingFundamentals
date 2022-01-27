# Part 1 – Practise using Lists

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,
9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,
63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

list_len = len(ages)
print(list_len)

for i in ages:
    print(i)

for i in ages:
    print(i+1)

for i in ages:
    if i < 16 or i > 65:
        ages.remove(i)
print(ages)

count = 0
for i in ages:
    if i > 15 and i < 26:
        count+=1
print(count)

ages.sort()
print(ages)

count = 0
for i in ages:
    if i > 15 and i < 26:
        count+=1
proportion = round(100*count/len(ages), 2)
print(f"{proportion}% are between 16-25")