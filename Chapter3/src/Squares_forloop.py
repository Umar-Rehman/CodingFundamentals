# Part 1 - Squares with a for loop

def square():
    for i in range(1, 101):
        if i**2 > 2000:
            print(f"The square of {i} is greater than 2000.")
            return i, i**2
        else:
            print(f"Number: {i}     Square{i**2}")

# To try the function yourself, uncomment the following lines:
# square()