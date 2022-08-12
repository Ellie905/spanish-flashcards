# Ellie Day
# 07/31/22

# Data from https://1000mostcommonwords.com/1000-most-common-spanish-words/


import json
import random


# Display Word, Get Response
def flashcards(words, en_otro):
    print()
    if en_otro:
        print('Escriba 1 para detenerse, escriba 2 para salir')
    else:
        print('Type 1 to stop, 2 to quit')
    print()

    resp = ''
    x = 0
    while not resp.isnumeric():
        word = random.choice(words)

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

    # Define
    words = dictionary

    first_word: int = 0
    last_word: int = 0

    # User selects to show Spanish or English words
    mode = ''

    while not mode.isnumeric():
        print()
        mode = input('Type 1 to display words in Spanish, Type 2 to display words in English: ')

    # Catch Value Errors
    try:
        first_word = int(input('Number of First Word: '))
        last_word = int(input('Number of Last Word: '))
        words = dictionary[first_word:last_word]
    except ValueError:
        print('Error: Value Error! Using all words!')

    # Catch invalid list indices
    if first_word <= -1 or last_word >= 1001:
        words = dictionary
        print('Error: Index Error! Using all words!')

    # Run list based on user's choice
    flashcards(words, bool(int(mode) - 2))


main()
