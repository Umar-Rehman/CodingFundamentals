import getpass
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

def showState(incorrect_letters, correct_letters, secret_word):
    print(f"{HANGMAN_PICS[len(incorrect_letters)]}\n")
    print(f"Guesses: {incorrect_letters+correct_letters}\n")

    revealed = "-"*len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            revealed = revealed[:i] + secret_word[i] + revealed[i+1:]

    print(f"Letters revealed: {revealed}\n")


def make_guess(guessed_already):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or bool(guess.isalpha) == False:
            print("Enter 1 letter!")
        elif guess in guessed_already:
            print("You've already guess this letter, choose another!")
        else:
            return guess

def play_game():
    incorrect_letters = ""
    correct_letters = ""

    secret_word = getpass.getpass("Enter the word: ")

    gameOver = False
    while not gameOver:
        showState(incorrect_letters, correct_letters, secret_word)

        guess = make_guess(incorrect_letters+correct_letters)

        if guess in secret_word:
            correct_letters+=guess
            guessed_all = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    guessed_all = False
                    break
                    
            if guessed_all:
                print(f"Well done, you win! The word was {secret_word}!")
                gameOver = True
        else:
            print("Incorrect!\n")
            incorrect_letters+=guess
            if len(incorrect_letters) == len(HANGMAN_PICS)-1:
                showState(incorrect_letters, correct_letters, secret_word)
                print(f"Unfortunate! You guessed {len(correct_letters)} correctly, alas, the word was actually {secret_word}!")
                gameOver = True

play_game()