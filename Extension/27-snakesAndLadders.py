# Snakes and Ladders

import random

def roll():
    roll = random.randint(1, 6)
    return roll

def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Player 1... Who are you? ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Player 2... Who are you? ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name

def play_round(player, position, count):
        
    print(f"{player} is at position: {position}")
    if position > 95:
        print(f"{player} needs to roll {100-position} or less to progress!")
    go = input("Hit enter to roll!")
    
    if go == "":
        roll_output = roll()
        count+=1
    
    if position+roll_output == 100:
        position+=roll_output
        print(f"{player} Wins!\nTotal moves: {count}")
        return position, count

    elif position+roll_output > 100:
        position-=roll_output
        print(f"{player} rolled {roll_output} and moves back instead!\nNew position: {position}")
        return position, count

    elif position%17 == 0 and position != 97:
        position+=12
        print(f"{player} advances {roll_output} spaces and climbs a ladder!\nNew position: {position}")
        return position, count
    elif position%13 == 0:
        position-=12
        print(f"{player} advances {roll_output} spaces and slides down a snake!\nNew position: {position}")
        return position, count
    else:
        position+=roll_output
        print(f"{player} advances {roll_output} spaces!\nNew position: {position}")
        return position, count

def play_game():
    player1_position = 1
    player2_position = 1
    player1_count = 0
    player2_count = 0

    player1, player2 = get_player_names()

    while True:
        player1_position, player1_count = play_round(player1, player1_position, player1_count)
        if player1_position == 100:
            break
        print("\n")
        player2_position, player2_count = play_round(player2, player2_position, player2_count)
        if player2_position == 100:
            break
        print("\n")

play_game()