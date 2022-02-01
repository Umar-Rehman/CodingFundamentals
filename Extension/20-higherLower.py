# Higher / lower

import random
from difflib import get_close_matches

def higher_lower():
    do = True
    while do:
        difficulty = input("Select a Difficulty or Quit:\n\n1. Normal\n2. Hard\n3. Quit Game\n\n")
        while type(difficulty) != int:
            try:
                difficulty = int(difficulty)
                if int(difficulty) < 1 or int(difficulty) > 3:
                    raise Exception
                else:
                    continue
            except:
                difficulty = input("Please enter an option between 1-3: ")

        if difficulty == 3:
            do = False
            break
    
        li = list(range(1,11))
        random.shuffle(li)

        persist = True
        matches = ["higher", "lower", "h", "l"]
        revealed = [li[0]]

        for i in range(1,10):
            revealed.append("?")

        while persist == True:
            print(f"\nFirst value: {li[0]}")
            for i in range(1, 10):
                guess = get_close_matches(input(f"\nHigher or Lower?: "), matches)
                
                bad_input = True
                while bad_input == True:
                    try:
                        guess = guess[0][0]
                        bad_input = False
                    except:
                        guess = get_close_matches(input("Didn't quite catch that...\nHigher or Lower?: "), matches)
                
                if guess == "h" and li[i] > li[i-1]:
                    if i == 9:
                        print("You Win!")
                        persist = False
                        break
                    else:
                        revealed[i] = li[i]
                        print(f"\nWell done!\nLevel {i+1}")
                        if difficulty == 1:
                            print(f"\nNumbers revealed: {revealed}")
                        continue
                elif guess == "l" and li[i] < li[i-1]:
                    if i == 9:
                        print("You Win!")
                        persist = False
                        break
                    else:
                        revealed[i] = li[i]
                        print(f"\nWell done!\nLevel {i+1}")
                        if difficulty == 1:
                            print(f"\nNumbers revealed: {revealed}")
                        continue
                else:
                    print(f"\nSorry, the next number was actually {'Higher' if li[i] > li[i-1] else 'Lower'} as it was {li[i]}!")
                    persist = False
                    print(f"\nYou got {len(list(i for i in revealed if isinstance(i, int)))-1} correct: {revealed}\n")
                    break

higher_lower()