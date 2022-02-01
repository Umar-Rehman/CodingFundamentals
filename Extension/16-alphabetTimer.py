# Alphabet timer

import time
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def alphabet_timer():
    print("I will record how fast you can enter each letter in the alphabet IN ORDER.\n")
    time.sleep(1)
    print("Ready..")
    time.sleep(1)
    print("Set..")
    time.sleep(1)
    print("GO!")
    start_time = time.time()
    i=0
    while i < 26:
        current_time = time.time()
        elapsed_time = current_time - start_time
        letter = input(f"Enter letter {i+1}: ").lower()
        if letter == alphabets[i]:
            i+=1
        else:
            print("Incorrect! Try Again.")
            continue
    print(f"You did it in {round(elapsed_time, 2)}s!")

alphabet_timer()