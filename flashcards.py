# Ellie Day
# 07/31/22

# Data from https://1000mostcommonwords.com/1000-most-common-spanish-words/


import argparse
import json
import random


# Display Word, Get Response
def flashcards(words, en_otro, sequence=False):
    print()
    if en_otro:
        print('Escriba 1 para detenerse, escriba 2 para salir')
    else:
        print('Type 1 to stop, 2 to quit')
    print()

    global word

    resp = ''
    x = 0
    while not resp.isnumeric():
        if sequence is False:
            word = random.choice(words)

        try:
            if sequence is True:
                word = words[x]
        except IndexError:
            x = 0
            continue


        # Display
        if en_otro is True:  # Display in Spanish
            print('ID: ' + word['Number'])
            print(word['Spanish'])
            print()

            resp = input('Escribe en inglés: ')

        if en_otro is False:  # Display in English
            print('Word Number: ' + word['Number'])
            print(word['in English'])
            print()

            resp = input('Write word in Spanish: ')

        if sequence is True:
            x += 1

        #if x + 1 > words

        # Check Response
        if (resp == word['Spanish'] and en_otro is False) or (resp == word['in English'] and en_otro is True):
            print('Correct!')
            print()
            continue

        # Show Results
        if en_otro is True:
            print('Ay, incorrecto. La palabra es: ' + word['in English'] + ', otra vez')

        if en_otro is False:
            print('Sorry, that\'s incorrect. The real word was: ' + word['Spanish'] + '; try again!')

        if not resp.isnumeric():
            print()
            continue

    # Restart or Quit
    if int(resp) == 2:
        exit(0)
    else:
        main()


def main():
    # Load File
    with open('spanish.json', 'r') as file:
        dictionary = json.load(file)

    # Define Args
    parser = argparse.ArgumentParser(description='Select values to choose how to display and which flashcards to '
                                                 'display')
    # Sequence or Random
    parser.add_argument(dest='arg1', metavar='A', type=int, help='Type 1 to display random words, Type 2 to display '
                                                                 'sequential words', default=1)
    # Type of Word Shown
    parser.add_argument(dest='arg2', metavar='B', type=int, help='Type 1 to display words in Spanish, Type 2 to '
                                                                 'display words in English', default=2)
    # Number of First Word
    parser.add_argument(dest='arg3', metavar='C', type=int, help='Value between 1 and 1000', default=1)
    # Number of Last Word
    parser.add_argument(dest='arg4', metavar='D', type=int, help='Value between First Word and 1000', default=150)

    parser.print_help()
    args = parser.parse_args()

    # Define Vars
    words = dictionary
    sequence = args.arg1
    mode: str = args.arg2
    first_word: int = int(args.arg3) - 1
    last_word: int = args.arg4

    # Catch Value Errors
    try:
        words = dictionary[first_word:last_word]
    except ValueError:
        print('Error: Value Error! Using all words!')

    # Catch invalid list indices
    if first_word <= -1 or last_word >= 1001:
        words = dictionary
        print('Error: Index Error! Using all words!')

    if int(sequence) == 2:
        sequence = True
    else:
        sequence = False

    # Run list based on user's choice
    flashcards(words, bool(int(mode) - 2), sequence)


main()
