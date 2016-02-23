#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#
# name: Sarah Larbi
# email: slarbi@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Sheryn Chung
# partner's email: sherync@bu.edu
#

from ps10pr1 import Board

# Write your Player class below.

class Player:
    
    def __init__(self, checker):
        '''constructs a new Player object'''
        
        assert(checker == 'X' or checker == 'O')
        self.num_moves = 0
        self.checker = checker

    def __str__(self):
        '''returns a string representing a Player object. '''

               
        s = 'Player '
        s += self.checker
        return s

    
    def __repr__(self):
        '''returns a string representing a Player object.'''

        return str(self)

    def opponent_checker(self):
        '''returns a one-character string representing the checker of the Player object’s opponent'''

        if self.checker == 'X':
            return 'O'

        return 'X'

    def next_move(self, board):
        '''accepts a Board object as a parameter and returns the column where the player wants to make the next move.'''

        x = int(input('Enter a colunm: '))

        while x < 0 or x > board.width - 1:
            print('Try again!')
            x = int(input('Enter a colunm: '))

        else:
            self.num_moves += 1
            return x
            

    
