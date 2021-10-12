
class Hangman: 
    def __init__(self, word, stages):
        self.word = word
        self.display = []
        self.lives = 6
        self.stage = stages
        self.missed_letters = []
#------------------------Copies The same amount of letters with '_' ---------------------------------------------

    def displayy(self):
        for x in self.word:
             self.display += '_'
             
#------------------------Checks if letter is in word ---------------------------------------------

    def word_check(self):
        guess = input('Guess a Word\n').lower()
        if guess in self.display or guess in self.missed_letters:
            print(f'You already guess this letter: {guess.upper()} bruh')
        length = len(self.word)
        for index in range(0, length):
            word_index = self.word[index]
            if guess == word_index:
                self.display[index] = word_index
        self.life(guess, self.word)
        print(f' Guessed letters: {self.missed_letters}')
        print(f"{' '.join(self.display)}")    #Reprint Display with new value or none
        print(self.stage[self.lives])
#------------------------Subtracts a lives when wrong ---------------------------------------------

    def life(self, guess, word):
        if guess not in word:
            self.lives -= 1
            self.missed_letters.append(guess)
            print(f'You Guess: {guess.upper()}, That Was Wrong You Lose a Life')

#------------------------Win Condition ---------------------------------------------

    def win(self):
        if '_' not in self.display:
            print('You Win')
            return True
#------------------------Lose Conditon ---------------------------------------------
            
    def lose(self):
        if self.lives == 0:
            print('You lose')
            return True
          



           
            





                




