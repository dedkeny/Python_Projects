#! /usr/bin/python3.11

import random


def get_num():

    user_input = input("\n\t :")

    if user_input.isdigit():
        return int(user_input)
    else:
        print("\nYou need to enter a number...")
        get_num()


print("\nWhat's the largest number I can choose?")
upper_bound = get_num()
number = random.randint(0, upper_bound)

print("\nHow many guesses do you want me to give you?")
guess_limit = get_num()

print("\nOkay, im thinking of a number between 0 & {0}\n\nYou have {1} guesses".format(
    str(upper_bound), str(guess_limit)))

guess_count = 0

while guess_count < guess_limit:

    print("\n\tYour guess?")
    guess = get_num()

    if guess == number:
        print("\nCorrect, YOU WIN!!!")
        break

    elif guess < number:
        print("\nToo low")
        guess_count += 1
        print("You have {} guesses left.".format(
            str(guess_limit - guess_count)))

    elif guess > number:
        print("\nToo high")
        guess_count += 1
        print("You have {} guesses left.".format(
            str(guess_limit - guess_count)))

    else:
        print("\nThe dev has a skill issue, idk what went wrong")

if guess_count >= guess_limit:
    print("\nSorry, YOU LOSE\n\nGoodbye")

exit
