# Ellie Day
# 07/31/22

# Spanish Words from https://1000mostcommonwords.com/1000-most-common-spanish-words/
# Russian Words from https://1000mostcommonwords.com/1000-most-common-russian-words/


import json
import random


# Display Word, Get Response
def flashcards(words, phrases, show_english, show_random=False):
    print()
    if not show_english:
        print(phrases['1'])
    else:
        print('Type 1 to stop, 2 to quit')
    print()

    word: any = words[0]

    resp = ''
    x = 0
    while not resp.isnumeric():
        if show_random is True:
            word = random.choice(words)

        try:
            if show_random is False:
                word = words[x]
        except IndexError:
            x = 0
            continue

        # Display
        if show_english is False:  # Display in Other Language
            print('ID: ' + word['Number'])
            print(word['Word'])
            print()

            resp = input(phrases['2'])

        if show_english is True:  # Display in English
            print('Word Number: ' + word['Number'])
            print(word['in English'])
            print()

            resp = input('Write word in Other Language: ')

        if show_random is False:
            x += 1

        # if x + 1 > words

        # Check Response
        if (resp == word['Word'] and show_english is True) or (resp == word['in English'] and show_english is False):
            print('Correct!')
            print()
            continue

        # If resp is a number, break out of loop
        if resp.isnumeric():
            continue

        # Show Results
        if show_english is False:
            print(phrases['3'] + word['in English'] + phrases['4'])

        if show_english is True:
            print('Sorry, that\'s incorrect. The real word was: ' + word['Word'] + '; try again!')

        if not resp.isnumeric():
            print()
            continue

    # Restart or Quit
    if int(resp) == 2:
        exit(0)
    else:
        main()


def settings():
    # Setting 3: all word types?
    # Setting 3.1: verbs?
    # Setting 3.2: adjectives? (otherwise nouns)

    # Vars
    show_english = True
    show_random = True

    # Setting 1
    print()

    print('Would you like to display all words in English (and guess the related word in another language?)')
    print('Y = Yes')
    print('N = No')
    temp_inp_var = str.upper(input())

    while not temp_inp_var == 'Y' and not temp_inp_var == 'N':
        temp_inp_var = str.upper(input())

    if temp_inp_var == 'Y':
        show_english = True  # Equal to arg2 = 2 from old code | Program is in English
    if temp_inp_var == 'N':
        show_english = False  # Equal to arg2 = 1 from old code | Program is in Other Language

    # Setting 2
    print()

    print('Display words in random order? (otherwise, sequential order)')

    temp_inp_var = str.upper(input())

    while not temp_inp_var == 'Y' and not temp_inp_var == 'N':
        temp_inp_var = str.upper(input())

    if temp_inp_var == 'Y':
        show_random = True
    if temp_inp_var == 'N':
        show_random = False

    # Setting 4
    print()

    print('Type the number of the first word (1-1000)')

    temp_inp_var = int(input())

    while not int(temp_inp_var) < 1000 and not int(temp_inp_var) > 0:
        temp_inp_var = int(input())

    first_number = temp_inp_var

    # Setting 5
    print()

    print('Type the number of the last word (1-1000)')

    temp_inp_var = int(input())

    while not int(temp_inp_var) < 1000 and not int(temp_inp_var) > first_number:
        temp_inp_var = int(input())

    final_number = temp_inp_var

    # Return Settings
    return show_english, show_random, (first_number - 1), (final_number - 1)


def main():
    # Load Phrases File
    with open('phrases.json', 'r') as file:
        phrases = json.load(file)

    # Choose Language
    language = ''

    print("Choose language:")
    print("1: Spanish")
    print("2: Russian")
    temp_inp_var = int(input())

    if temp_inp_var == 1:
        language = 'spanish.json'
        phrases = phrases[0]
    if temp_inp_var == 2:
        language = 'russian.json'
        phrases = phrases[1]

    while not temp_inp_var < 2 and not temp_inp_var > 1:
        temp_inp_var = int(input())

    # Load Language File
    with open(language, 'r') as file:
        dictionary = json.load(file)

    # Define Vars
    words = dictionary
    show_english, show_random, first_number, final_number = settings()

    # Catch Value Errors
    try:
        words = dictionary[first_number:final_number]
    except ValueError:
        print('Error: Value Error! Using all words!')

    # Run list based on user's choice
    flashcards(words, phrases, show_english, show_random)


main()
