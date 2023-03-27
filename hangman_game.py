import os
import random
import time
from functools import reduce


def logo_hangman():
    print('''

    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   █   █   █████   █   █   █████   █   █   █████   █   █   ║
    ║   █   █   █   █   ██  █   █       ██ ██   █   █   ██  █   ║
    ║   █████   █████   █ █ █   █████   █ █ █   █████   █ █ █   ║
    ║   █   █   █   █   █  ██   █   █   █   █   █   █   █  ██   ║
    ║   █   █   █   █   █   █   █████   █   █   █   █   █   █   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
''')


def image_hangman():
    die0 = '''













'''
    die1 = '''







        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die2 = '''
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die3 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die4 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die5 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    / \
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die6 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║     │
          ║    / \
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die7 = '''
          ╔═════╦  
          ║
          ║
          ║    ─┼─
          ║     │
          ║    / \
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die8 = '''
          ╔═════╦  
          ║
          ║
          ║   ┌─┼─┐
          ║     │
          ║    / \
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die9 = '''
          ╔═════╦  
          ║
          ║     @
          ║   ┌─┼─┐
          ║     │
          ║    / \
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die10 = '''
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / \
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die11 = '''
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡GANASTE!
          ║
          ║                  
        __║__________        @
      /   ║         /|     └─┼─┘  
     /____________ / |       │
    |             | /       / \
    |_____________|/       d   b

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10,
              11: die11}
    return deaths


def select_random_word():

    # 1. Selecciona una palabra al azar de un archivo
    with open('./archivos/data.txt', 'r', encoding='utf-8') as data_words:
        word = random.choice([word.strip().upper() for word in data_words])

    # 2. Mete las letras de la palabra a una lista y elimina las tildes
    vowels = {'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}

    for letter in word:
        for key in vowels:
            if letter == key:
                word = word.replace(letter, vowels[key])

    # 3. Convierte la lista a string
    return word


def new_word(word, discovered, deaths, letters):
    print("-------------")
    print(f"word => {word}")
    print(f"discovered => {discovered}")
    print(f"deaths => {deaths}")
    print(f"letters => {letters}")
    word = select_random_word()
    discovered = ['- '] * len(word)
    deaths = 0
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
               'X', 'Y', 'Z']
    return word, discovered, deaths, letters


def compare_letter(letter, word, discovered):
    """
    Compara si la letra ingresada está en la palabra

    :param letter: letra ingresada
    :param word: palabra elegida al azar
    :param discovered: Muestra letras descubiertas y espacios (-) en las que no han sido descubiertas
    :return:
    """
    fail = True
    for l in range(len(word)):
        if word[l] == letter:
            discovered[l] = letter + ' '
            fail = False
    return discovered, fail


def refresh(hangman_deaths, deaths, letters):
    """
    Muestra dibujo de acuerdo a la etapa
    :param hangman_deaths:
    :param deaths:
    :param letters:
    :return:
    """
    # os.system('clear')
    logo_hangman()
    print('Letras disponibles: ' + "  ".join(letters))
    print(hangman_deaths.get(deaths))


class Hangman:
    def __int__(self):
        pass


def run():
    # 1. Diccionario de etapas del ahorcado
    hangman_deaths = image_hangman()

    # 2. Inicializa variables
    word = ''
    discovered = []
    deaths = 0
    letters = []
    word, discovered, deaths, letters = new_word(word, discovered, deaths, letters)

    while True:
        refresh(hangman_deaths, deaths, letters)

        # 3. Pide letra y la valida
        letter = input('''¡Adivina la palabra!     ''' + ''.join(discovered) + '''\nIngresa una letra: ''').upper()
        if letter not in letters:
            print('Debes ingresar una de las letras disponibles')
        else:
            letters[letters.index(letter)] = ''

        discovered, fail = compare_letter(letter, word, discovered)

        if fail:
            deaths += 1

        # se ahorcó
        if deaths == 10:
            refresh(hangman_deaths, deaths, letters)
            print('¡Perdiste! La palabra era ' + word)

        # ganó
        if ''.join(discovered).replace(' ', '') == word:
            refresh(hangman_deaths, 11, letters)
            print('¡Ganaste!, Tuviste ', deaths, ' erorres      ' + ''.join(discovered))

        # Preguntar si desea volver a jugar
        if deaths == 10 or ''.join(discovered).replace(' ', '') == word:

            again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
            if again == '1':
                word, discovered, deaths, letters = new_word(word, discovered, deaths, letters)
                continue
            else:
                print('Gracias por jugar :)')
                break


if __name__ == '__main__':
    # os.system('clear')
    run()
