#! /usr/bin/python3.11
# Code rendition of the game "Bulls & Cows"

import random

secret_Code = list(str(random.randint(1000, 10000)))


def get_Num():
    player_input = input(": ")
    if player_input in ['q', 'quit']:
        quit()
    elif player_input.isdigit():
        if 999 < int(player_input) < 10000:
            return player_input
        else:
            print("\nYou need to give me a 4-digit number...")
            get_Num()
    else:
        print("\nYou need to give me your number in digits...")
        get_Num()


def get_Bulls(guess):
    bulls = 0
    for i in range(0, 4):
        guessA = int(guess[i])
        secretA = int(secret_Code[i])
        if secretA == guessA:
            bulls += 1
    return bulls


def get_Cows(guess):
    cows = 0
    for n in range(10):
        if str(n) in guess and secret_Code:
            cows += 1
        n += 1
    return cows


def game():
    global secret_Code
    tries = 19
    while tries > 0:
        guess = get_guess()
        if guess == secret_Code:
            print("That is correct, YOU WIN!")
            break
        else:
            bulls = get_Bulls(guess)
            cows = get_Cows(guess)
        print("there were:\n\t{0} Bulls\n\t{1} Cows\n\nYou have {2} tries left.\n\n".format(
            bulls, cows, tries))
        tries -= 1


def get_guess():
    guess = list(str(get_Num()))
    return guess


def start():
    print("I'm thinking of a 4 digit number, can you guess what it is?"
          + "\nRules:"
            + "\n\tI think of a 4-digit number."
            + "\n\tYou try to guess the number."
            + "\n\tI give you hints about the digits of your guess"
            + "\n\t\t(X) Bulls = (X) correct numbers in correct positions."
            + "\n\t\t(X) Cows  = (X) correct numbers in wrong positions."
            + "\n\nYou have 20 chances to guess the correct number."
            + '\nGuess "quit" to exit the game.'
            + "\n\nWhat is your first guess?")

    game()


if __name__ == "__main__":
    start()
