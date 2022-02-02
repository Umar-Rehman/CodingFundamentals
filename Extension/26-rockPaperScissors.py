# Rock Paper Scissors

# GAME RULES:

# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors


class Rules():
    Rule1 = '- Scissors cuts Paper'
    Rule2 = '- Paper covers Rock'
    Rule3 = '- Spock smashes Scissors'
    Rule4 = '- Scissors decapitates Lizard'
    Rule5 = '- Lizard eats Paper'
    Rule6 = '- Paper disproves Spock'
    Rule7 = '- Spock vaporizes Rock'
    Rule8 = '- (and as it always has) Rock crushes Scissors'


print(
    f"First time playing Rock Paper Scissors Lizard Spock? How does it work, you ask?\n\nOh it's very simple:\n\n{Rules.Rule1}\n{Rules.Rule2}\n{Rules.Rule3}\n{Rules.Rule4}\n{Rules.Rule5}\n{Rules.Rule6}\n{Rules.Rule7}\n{Rules.Rule8}\n\nLet's begin..."
)
import random
from enum import IntEnum


# Defines a class with values assigned to each choice
class Choice(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3
    Lizard = 4
    Spock = 5


# Defines the win conditions in an object
win_condition = {
    Choice.Scissors: [Choice.Lizard, Choice.Paper],
    Choice.Paper: [Choice.Spock, Choice.Rock],
    Choice.Rock: [Choice.Lizard, Choice.Scissors],
    Choice.Lizard: [Choice.Spock, Choice.Paper],
    Choice.Spock: [Choice.Scissors, Choice.Rock]
}


# Gets users choice
def user1_choice():
    choices = [f"{action.name}[{action.value}]" for action in Choice]
    choices_str = ", ".join(choices)
    selection = int(input(f"\nPlayer 1: Make your choice ({choices_str}): "))
    action = Choice(selection)
    return action


# Randomizes computers choice
def comp_choice():
    selection = random.randint(1, len(Choice))
    action = Choice(selection)
    return action

def user2_choice():
    choices = [f"{action.name}[{action.value}]" for action in Choice]
    choices_str = ", ".join(choices)
    selection = int(input(f"\nPlayer 2: Make your choice ({choices_str}): "))
    action = Choice(selection)
    return action

# Finds the winner of the round
def who_wins(user1_action, user2_action):
    if user1_action == user2_action:
        print(f"\nYou both picked {user1_action.name}. It's a tie!\n")

    # All possible outcomes if user picks ROCK
    if user1_action == Choice.Rock:

        if user2_action == Choice.Scissors:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Rock smashes Scissors!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Lizard:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Rock crushes Lizard!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Paper:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Paper covers Rock! \n\nPlayer 2 wins!\n"
            )
        elif user2_action == Choice.Spock:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Spock vaporizes Rock! \n\nPlayer 2 wins!\n"
            )

    # All possible outcomes if user picks PAPER
    elif user1_action == Choice.Paper:

        if user2_action == Choice.Rock:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Paper covers Rock!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Spock:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Paper disproves Spock!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Scissors:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Scissors cuts Paper! \n\nPlayer 2 wins!\n"
            )
        elif user2_action == Choice.Lizard:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Lizard eats Paper! \n\nPlayer 2 wins!\n"
            )

    # All possible outcomes if user picks SCISSORS
    elif user1_action == Choice.Scissors:

        if user2_action == Choice.Paper:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Scissors cuts paper!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Lizard:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Scissors decapitates Lizard!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Rock:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Rock smashes scissors! \n\nPlayer 2 wins!\n"
            )
        elif user2_action == Choice.Spock:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Spock smashes Scissors! \n\nPlayer 2 wins!\n"
            )

    # All possible outcomes if user picks LIZARD
    elif user1_action == Choice.Lizard:

        if user2_action == Choice.Paper:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Lizard eats paper!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Spock:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Lizard poisons Spock!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Rock:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Rock crushes Lizard! \n\nPlayer 2 wins!\n"
            )
        elif user2_action == Choice.Scissors:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Scissors decapitates Lizard! \n\nPlayer 2 wins!\n"
            )

    # All possible outcomes if user picks SPOCK
    elif user1_action == Choice.Spock:

        if user2_action == Choice.Scissors:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Spock smashes Scissors!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Rock:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Spock vaporizes Rock!\n\nPlayer 1 wins!\n"
            )
        elif user2_action == Choice.Paper:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Paper disproves Spock! \n\nPlayer 2 wins!\n"
            )
        elif user2_action == Choice.Lizard:
            print(
                f"\nPlayer 1 chose {user1_action.name} and Player 2 chose {user2_action.name}, and everyone knows that Lizard poisons Spock! \n\nPlayer 2 wins!\n"
            )


# Validates choice input to be within the range of the options available in the class Choice. Calls the main functions to get user choice, comp choice and compares them to find a winner. Includes a 'Play again?' loop.
def play_game():

    while True:

        option = input("Modes:\n1. 1-Player\n2. 2-Player\nChoose a mode: ")
        while type(option) != int:
            try:
                option = int(option)
                if int(option) < 1 or int(option) > 8:
                    raise Exception
                else:
                    continue
            except:
                option = input("Please enter an option between 1-2: ")
        
        try:
            user1_action = user1_choice()
        except ValueError:
            range_str = f"[1, {len(Choice)}]"
            print(f"\nInvalid selection. Enter a value in range {range_str}\n")
            continue
        
        if option == 2:
            try:
                user2_action = user2_choice()
            except ValueError:
                range_str = f"[1, {len(Choice)}]"
                print(f"\nInvalid selection. Enter a value in range {range_str}\n")
                continue
        else:
            user2_action = comp_choice()

        who_wins(user1_action, user2_action)

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

play_game()