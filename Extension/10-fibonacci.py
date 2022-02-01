# Fibonacci generator

def fibonacci():

    li = [0, 1, 1]
    for i in range(3, 50):
        li.append(li[-1]+li[-2])
    
    print(li)

fibonacci()