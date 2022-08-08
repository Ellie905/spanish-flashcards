# Ellie Day
# 07/31/22

# Data from https://1000mostcommonwords.com/1000-most-common-spanish-words/


import json
import random


def main():
    with open('spanish.json', 'r') as file:
        dictionary = json.load(file)

    words = dictionary

    first_word: int = 0
    last_word: int = 0

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

    print()
    print('Type 1 to stop, 2 to quit')
    print()

    resp = ''
    x = 0
    while not resp.isnumeric():
        word = random.choice(words)

        print('Word Number: ' + word['Number'])
        print(word['in English'])
        print()

        resp = input('Write word in Spanish: ')

        if resp == word['Spanish']:
            print('Correct!')
            print()
            continue

        if not resp.isnumeric():
            print('Sorry, that\'s incorrect. The real word was: ' + word['Spanish'] + '; try again!')
            print()
            continue

    if int(resp) == 2:
        exit(0)
    else:
        main()


main()
