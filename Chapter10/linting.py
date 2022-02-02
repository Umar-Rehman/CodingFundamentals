# Linting
"""Linting"""

def count(sequence, item):
    """This method counts the number of occurences of {item} inside the {sequence}"""
    num_occurences = 0
    for each_item in sequence:
        if each_item == item:
            num_occurences += 1
    return num_occurences

print(count("Hello, World!", "l"))
