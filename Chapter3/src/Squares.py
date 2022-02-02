# Part 1 - Squares

def while_square():
    x=1
    while x <= 100:
        if x**2 <= 2000:
            print(f"{x}: {x**2}")
            x+=1
        else:
            return(x)

# To try the function yourself, uncomment the following lines:
# while_square()