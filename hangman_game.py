import os
import random


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
          ║    / ''' + chr(92) + '''
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
          ║    / ''' + chr(92) + '''
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
          ║    / ''' + chr(92) + '''
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
          ║    / ''' + chr(92) + '''
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
          ║    / ''' + chr(92) + '''
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
          ║    / ''' + chr(92) + '''
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
    |             | /       / ''' + chr(92) + '''
    |_____________|/       d   b

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10,
              11: die11}
    return deaths


def choose_random_word():
    # Selecciona una palabra al azar de un archivo
    with open('./archivos/data.txt', 'r', encoding='utf-8') as data_words:
        word = random.choice([word.strip().upper() for word in data_words])

    # Mete las letras de la palabra a una lista y elimina las tildes
    vowels = {'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}

    for letter in word:
        for key in vowels:
            if letter == key:
                word = word.replace(letter, vowels[key])

    # Convierte la lista a string
    return word


class Hangman:
    """
    word: palabra elegida al azar
    discovered: Muestra letras descubiertas y espacios (-) en las que no han sido descubiertas
    """

    def __init__(self):

        # Inicializa variables
        self.word = choose_random_word()
        self.discovered = ['- '] * len(self.word)
        self.deaths = 0
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
                        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def compare_letter(self, letter):
        """
        Compara si la letra ingresada está en la palabra
        :param letter: letra ingresada
        :return:
        """
        if letter not in self.letters:
            print('Debes ingresar una de las letras disponibles')
        else:
            self.letters[self.letters.index(letter)] = ''
        fail = True

        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.discovered[i] = letter + ' '
                fail = False

        if fail:
            self.deaths += 1

    def is_alive(self):
        """
        si se ahorcó o no
        :return:
        """
        if self.deaths == 10:
            return False
        else:
            return True


def run():
    hangman = Hangman()

    # Diccionario de etapas del ahorcado
    hangman_deaths = image_hangman()

    while True:
        os.system('clear')
        logo_hangman()
        print('Letras disponibles: ' + "  ".join(hangman.letters))
        print(hangman_deaths.get(hangman.deaths))

        # Pide letra
        letter = input(
            '''¡Adivina la palabra!     ''' + ''.join(hangman.discovered) + '''\nIngresa una letra: ''').upper()

        hangman.compare_letter(letter)

        if not hangman.is_alive():
            os.system('clear')
            logo_hangman()
            print(hangman_deaths.get(hangman.deaths))
            print('¡Perdiste! La palabra era ' + hangman.word)
            break

        # ganó
        if ''.join(hangman.discovered).replace(' ', '') == hangman.word:
            os.system('clear')
            logo_hangman()
            print(hangman_deaths.get(11))
            print('¡Ganaste!, Tuviste ', hangman.deaths, ' erorres      ' + ''.join(hangman.discovered))
            break


if __name__ == '__main__':
    os.system('clear')
    run()
    while True:
        # Pregunta si desea volver a jugar
        again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
        if again == '1':
            run()
        else:
            print('Gracias por jugar :)')
            break
