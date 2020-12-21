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


def main():
    """
    TODO:
    """
    ans = random_word()
    dash1 = dash(ans)
    print('Your word looks like: ' + dash1)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    your_guess(ans, dash1)


def dash(ans):
    dash1 = ''
    for i in range(len(ans)):
        dash1 += '-'
    return dash1


def your_guess(ans, dash1):
    chance = N_TURNS
    while True:
        guess = input('Your guess: ')
        if guess.isalpha() and len(guess) == 1:
            guess = guess.lower()
            if ans.find(guess) != -1:
                print("You are correct!")
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
