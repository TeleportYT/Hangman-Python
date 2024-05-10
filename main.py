import random

GUESSED_LETTERS = ['s', 'p', 'j', 'i', 'm', 'k']
NUM_OF_GUESS = 6;
'''random.randint(5, 11)'''
GAME_PARTS = ["""x-------x""", """    x-------x
    |
    |
    |
    |
    |
""", """    x-------x
    |       |
    |       0
    |
    |
    |""", """    x-------x
    |       |
    |       0
    |       |
    |
    |
""", """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", """    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
""", """    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""]


def print_status():
    print(GAME_PARTS[NUM_OF_GUESS - 6])


def guess_letter():
    letter = input("Guess a letter ")
    if len(letter) > 1:
        if not letter.isalpha():
            print("E3")
        else:
            print("E1")
    elif not letter.isalpha():
        print("E2")
    else:
        print(letter.lower())


def is_valid_input(letter_guessed):
    return True if letter_guessed.isalpha() and len(letter_guessed) == 1 else False


def check_valid_input(letter_guessed, old_letters_guessed):
    return is_valid_input(letter_guessed) and not old_letters_guessed.__contains__(letter_guessed)


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print(letter_guessed)
    for letter in old_letters_guessed: print(
        f"{letter if letter is not None else ""} {"-> " if old_letters_guessed.index(letter) != len(old_letters_guessed) - 1 else '\n'}",
        end="")
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for letter in secret_word:
        result += f"{letter} " if old_letters_guessed.__contains__(letter) else "_ "
    return result


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word :
        if not old_letters_guessed.__contains__(letter): return False
    return True

def enterWord():
    word = input("Please enter a word: ")
    print("_ " * len(word))


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
    print(try_update_letter_guessed(input("Enter a letter: "), GUESSED_LETTERS))
    print(try_update_letter_guessed(input("Enter a letter: "), GUESSED_LETTERS))
    print(show_hidden_word("mammals", GUESSED_LETTERS))
    print(check_win("kim", GUESSED_LETTERS))
    enterWord()


if __name__ == "__main__":
    main()
