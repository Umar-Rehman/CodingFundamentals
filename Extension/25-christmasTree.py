# Christmas Tree

def christmas_tree(size):
    for i in range(size):
        for j in range(size-i):
            print(' ', end='')
        for k in range(2*i+1):
            print("*", end= "")
        print()

    for i in range(2):
        for j in range(size-1):
            print("", end=" ")
        print(" * ")

christmas_tree(3)