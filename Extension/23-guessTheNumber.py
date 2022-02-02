# Guess the number

import random


def guess_number():
    count = 0
    lives = 5
    goal = random.randint(1,100)
    print(goal)
    while count < 5:
        guess = input("Enter your guess: ")
        while type(guess) != int:
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    raise Exception
                else:
                    continue
            except:
                guess = input("Please enter an integer value between 1-100: ")
        
        if guess > goal:
            count+=1
            lives-=1
            print(f"\nToo High!\nLives remaining: {lives}\n")
            
        elif guess < goal:
            count+=1
            lives-=1
            print(f"\nToo Low!\nLives remaining: {lives}\n")
            
        else:
            print(f"\nWell done! You guessed right in {count+1} attempt(s)!")
            break
    
    if count == 5:
        print(f"Better luck next time... you ran out of lives! The answer was {goal}")

guess_number()