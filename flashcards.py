# Ellie Day
# 07/31/22

# Data from https://1000mostcommonwords.com/1000-most-common-spanish-words/


import argparse
import json
import random


# Display Word, Get Response
def flashcards(words, show_english, show_random=False):
    print()
    if not show_english:
        print('Escriba 1 para detenerse, escriba 2 para salir')
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
        if show_english is False:  # Display in Spanish
            print('ID: ' + word['Number'])
            print(word['Spanish'])
            print()

            resp = input('Escribe en inglés: ')

        if show_english is True:  # Display in English
            print('Word Number: ' + word['Number'])
            print(word['in English'])
            print()

            resp = input('Write word in Spanish: ')

        if show_random is False:
            x += 1

        # if x + 1 > words

        # Check Response
        if (resp == word['Spanish'] and show_english is False) or (resp == word['in English'] and show_english is True):
            print('Correct!')
            print()
            continue

        # Show Results
        if show_english is False:
            print('Ay, incorrecto. La palabra es: ' + word['in English'] + ', otra vez')

        if show_english is True:
            print('Sorry, that\'s incorrect. The real word was: ' + word['Spanish'] + '; try again!')

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
    first_number = 1
    final_number = 1000

    print('Welcome to the English/Spanish Flashcards Tool!')
    print('Bienvenido a la herramienta de los palabras de íngles/español!')

    # Setting 1
    print()

    print('Would you like to display all words in English (and guess the related Spanish word?)')
    print('¿Quieres mostrar las palabras en íngles? (¿y adivinas la palabra español?)')
    print('Y = Yes | Y = sí')
    print('N = No')
    temp_inp_var = str.upper(input())

    while not temp_inp_var == 'Y' and not temp_inp_var == 'N':
        temp_inp_var = str.upper(input())

    if temp_inp_var == 'Y':
        show_english = True  # Equal to arg2 = 2 from old code | Program is in English
    if temp_inp_var == 'N':
        show_english = False  # Equal to arg2 = 1 from old code | Program is in Spanish

    # Setting 2
    print()

    if show_english:
        print('Display words in random order? (otherwise, sequential order)')
    else:
        print('¿Quieres mostrar las palabras en orden aleatorio? (la alternativa es el orden secuencial)')

    temp_inp_var = str.upper(input())

    while not temp_inp_var == 'Y' and not temp_inp_var == 'N':
        temp_inp_var = str.upper(input())

    if temp_inp_var == 'Y':
        show_random = True
    if temp_inp_var == 'N':
        show_random = False

    # Setting 4
    print()

    if show_english:
        print('Type the number of the first word (1-1000)')
    else:
        print('Escribe el número de la primera palabra (1-1000)')

    temp_inp_var = int(input())

    while not int(temp_inp_var) < 1000 and not int(temp_inp_var) > 0:
        temp_inp_var = int(input())

    first_number = temp_inp_var

    # Setting 5
    print()

    if show_english:
        print('Type the number of the last word (1-1000)')
    else:
        print('Escribe el número de la última palabra (1-1000)')

    temp_inp_var = int(input())

    while not int(temp_inp_var) < 1000 and not int(temp_inp_var) > first_number:
        temp_inp_var = int(input())

    final_number = temp_inp_var

    # Return Settings
    return show_english, show_random, (first_number - 1), (final_number - 1)


def main():
    # Load File
    with open('spanish.json', 'r') as file:
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
    flashcards(words, show_english, show_random)


main()
