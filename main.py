import random
SECRET_WORD = ""
GUESSED_LETTERS = []
NUM_OF_GUESS = 6;
'''random.randint(5, 11)'''
GAME_PARTS = {6: """x-------x""", 5: """    x-------x
    |
    |
    |
    |
    |
""", 4: """    x-------x
    |       |
    |       0
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 2: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 1: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", 0: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


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
    for letter in secret_word:
        if not old_letters_guessed.__contains__(letter): return False
    return True


def enterWord():
    word = input("Please enter a word: ")
    print("_ " * len(word))


def print_hangman(num_of_tries):
    print(GAME_PARTS[num_of_tries])


def choose_word(file_path, index):
    f = open(file_path)
    words = list(f.read().split(" "))
    f.close()
    return (len(words), words[(index - 1) % len(words)])


def setup_game():
    filePath = input("Please enter the file path: ")
    index = int(input("Please enter the index of the word: "))
    global SECRET_WORD
    SECRET_WORD = choose_word(filePath, index)[1]
    global GUESSED_LETTERS
    GUESSED_LETTERS = []
    print("_ " * len(SECRET_WORD))


def check_letter_inword(secret_word,letter_guessed):
    return secret_word.__contains__(letter_guessed)

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
    setup_game()
    global NUM_OF_GUESS, GUESSED_LETTERS,SECRET_WORD

    print(f"You have {NUM_OF_GUESS} guesses")
    while NUM_OF_GUESS>0 and not check_win(SECRET_WORD,GUESSED_LETTERS):
        letter = input("Enter a letter: ")
        if not try_update_letter_guessed(letter,GUESSED_LETTERS) or not check_letter_inword(SECRET_WORD,letter):
            print('wrong input try again')
            NUM_OF_GUESS -= 1

        print_hangman(NUM_OF_GUESS)
        print(show_hidden_word(SECRET_WORD, GUESSED_LETTERS))
    if check_win(SECRET_WORD,GUESSED_LETTERS):
        print("Congrats! You win!")
    else:
        print("Sorry, you lose :(")
        print("The word was " + SECRET_WORD)

if __name__ == "__main__":
    main()
