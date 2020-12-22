"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7
chance = N_TURNS


def main():
    """
    TODO:
    """
    ans = random_word()
    dash1 = dash(ans)
    draw()
    print('Your word looks like: ' + dash1)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    your_guess(ans, dash1)


def dash(ans):
    dash1 = ''
    for i in range(len(ans)):
        dash1 += '-'
    return dash1


def draw():
    global chance
    if chance == N_TURNS:
        print('    ----------\n    | /\n    |\n    |\n    |\n    |\n    |\n    |\n    |')
        print('____|____')
    elif chance == N_TURNS-1:
        print('    ----------\n    | /      |\n    |\n    |\n    |\n    |\n    |\n    |\n    |')
        print('____|____')
    elif chance == N_TURNS-2:
        print('    ----------\n    | /      |\n    |     (     )\n    |\n    |\n    |\n    |\n    |\n    |')
        print('____|____')
    elif chance == N_TURNS-3:
        print('    ----------\n    | /      |\n    |     ( X_X )\n    |\n    |\n    |\n    |\n    |\n    |')
        print('____|____')
    elif chance == N_TURNS-4:
        print('    ----------\n    | /      |\n    |     ( X_X )\n    |        |\n    |        |\n    |        |\n    |\n    |\n    |')
        print('____|____')
    elif chance == N_TURNS-5:
        print('    ----------\n    | /      |\n    |     ( X_X )\n    |        |\n    |      / | \\\n    |     o  |  o\n    |\n    |\n    |')
        print('____|____')
    elif chance == N_TURNS-6:
        print('    ----------\n    | /      |\n    |     ( X_X )\n    |        |\n    |      / | \\\n    |     o  |  o\n    |       / \\\n    |      /   \\\n    |')
        print('____|____')
    else:
        print('    ----------\n    | /      |\n    |     ( X_X )\n    |        |\n    |      / | \\\n    |     o  |  o\n    |       / \\\n    |      /   \\\n    |     =     =')
        print('____|____')


def your_guess(ans, dash1):
    global chance
    while True:
        guess = input('Your guess: ')
        if guess.isalpha() and len(guess) == 1:
            guess = guess.lower()
            if ans.find(guess) != -1:
                print("You are correct!")
                draw()
                dash2 = ''
                for i in range(len(ans)):
                    ch = ans[i]
                    if ch == guess:
                        dash2 += guess
                    else:
                        dash2 += dash1[i]
                dash1 = dash2
                if dash1.find('-') != -1:
                    print("The word looks like: " + dash1)
                    print("You have " + str(chance) + " guesses left.")
                elif dash1.find('-') == -1:
                    print("You win!!")
                    print("The word was: " + ans)
                    break
            elif ans.find(guess) == -1:
                print("There is no " + guess + "\'s in the word.")
                chance -= 1
                draw()
                if chance != 0:
                    print("You have " + str(chance) + " guesses left.")
                elif chance == 0:
                    print("You are completely hung : (")
                    print('The word is ' + ans)
                    break
        elif guess.isalpha() == 0 or len(guess) != 1:
            print("illegal format.")


def random_word():
    word_list = []
    with open('dictionary.txt', 'r') as f:
        for line in f:
            if len(line) >= 4:
                word_list.append(line)
    num = random.choice(range(len(word_list)))
    return word_list[num]


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
