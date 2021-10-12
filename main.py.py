import random
from hangman_words import word_list
from hangman_art import stages, logo
from hangmanClass import Hangman
import os
 


#------------------------Randmonize Word from list ---------------------------------------------
def rand_word():
    return random.choice(word_list)

#------------------------Hangman Game ---------------------------------------------

def game():
    print(logo)
    random_word = rand_word()
    hangman = Hangman(random_word, stages)
    hangman.displayy()
    while playagain:
        hangman.word_check()
        if hangman.win() or hangman.lose():
            break


playagain = 'y'
while playagain == 'y':
    os.system("cls") # Windows clear screen   
    game() # Hangman game
    playagain = input('Want to Go another Round?').lower() #Askes to play again

