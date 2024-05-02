import random

NUM_OF_GUESS = 6 ;'''random.randint(5, 11)'''
GAME_PARTS = ["""x-------x""","""    x-------x
    |
    |
    |
    |
    |
""","""    x-------x
    |       |
    |       0
    |
    |
    |""","""    x-------x
    |       |
    |       0
    |       |
    |
    |
""","""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""","""    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
""","""    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""]
def printStatus():
    print(GAME_PARTS[NUM_OF_GUESS-6])

def guessLetter():
    letter = input("Guess a letter ")
    print(letter.lower())

def enterWord():
    word = input("Please enter a word: ")
    print("_ "*len(word))

def main():
    print("Welcome to the game Hangman")
    print("""    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/""")
    print(f"You have {NUM_OF_GUESS} guesses")

    enterWord()

if __name__ == "__main__":
    main()