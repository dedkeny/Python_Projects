
#! /usr/bin/python
import random

# Opening reminder of game rules for no reason really...
print("Winning conditions of ROCK PAPER SCISSORS are:\n"
      + "\tPaper covers Rock\n"
      + "\tRock crushes Sciccors\n"
      + "\tScissors cuts Paper\n")

player_score = 0
comp_score = 0

def rematch():
    print("The score is:\n\tYou: {0}\n\tMe:  {1}".format(str(player_score), str(comp_score)))
    start = input("Would you like to play again?\n\t: ")

    if start.lower() in ['yes', 'y']:
        print('game starting...')
        match()

    elif start.lower() in ['no', 'n']:
        print('exiting...')
        exit
    else:
        print("I need a 'yes', 'y', 'no', or 'n' (not case sensitive)")
        rematch()

def comp_choice():

    comp_int = random.randint(1,3)

    if comp_int == 1:
        comp_word = 'Rock'

    elif comp_int == 2:
        comp_word = 'Paper'

    else:
        comp_word = 'Scissors'

    return comp_word

def player_choice():

    player_choice = input('(R)ock (P)aper or (S)cissors?\n\t:')

    if player_choice.lower() in ['s', 'scissors']:
        player_word == 'Scissors'

    elif player_choice.lower() in ['p', 'paper']:
        player_word = 'Paper'

    elif player_choice.lower() in ['r', 'rock']:
        player_word = 'Rock'

    else:
        print("I didn't understand that...\nRock it is then.\n")
        player_word = 'Rock'

    return player_word

def match():

    global player_score
    global comp_score

    comp_word = comp_choice()
    player_word = player_choice()

    if comp_word == player_word:
        print("We both chose {}, it's a Draw!".format(player_word))
        rematch()

    elif comp_word == 'Rock':

        if player_word == 'Scissors':
            comp_score += 1
            print('Rock crushes Scissors...\n\tSorry, you LOSE.')
            rematch()

        elif player_word == 'Paper':
            player_score += 1
            print('Paper covers Rock!\n\tYou WIN!')
            rematch()

    elif comp_word == 'Paper':

        if player_word == 'Rock':
            comp_score += 1
            print('Paper covers Rock...\n\tSorry, you LOSE.')
            rematch()

        elif player_word == 'Scissors':
            player_score += 1
            print('Scissors cuts Paper!\n\tYou WIN!')
            rematch()

    elif comp_word == 'Scissors':

        if player_word == 'Paper':
            comp_score += 1
            print('Scissors cuts Paper...\n\tSorry, you LOSE.')
            rematch()

        elif player_word == 'Rock':
            player_score += 1
            print('Rock crushes Scissors!\n\tYou WIN!')
            rematch()

    return

if __name__ == "__main__":
    match()
