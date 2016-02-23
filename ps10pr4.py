#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# An AI Player for Connect Four
#
# name: Sarah Larbi
# email: slarbi@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Sheryn Chung
# partner's email: sherync@bu.edu

#

from ps10pr3 import *
import random


class AIPlayer(Player):
    """intelligent computer player"""

    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object."""

        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        Player.__init__(self, checker)


    def __str__(self):
        """returns a string representing an AIPlayer object. """
        s = 'Player '
        s += self.checker
        s += ' ('
        s += self.tiebreak
        s += ', '
        s += str(self.lookahead)
        s += ')'
        return s

    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score. If one or more columns are tied for the maximum score, the method should apply the called AIPlayer‘s tiebreaking strategy to break the tie."""
        index = []
        max_score = max(scores)
        for x in range(len(scores)):
            if scores[x] == max_score:
                index += [x]

        if self.tiebreak == 'LEFT':
            return index[0]

        elif self.tiebreak == 'RIGHT':
            return index[-1]

        else:
            return random.choice(index)

    def scores_for(self, board):
        """ takes a Board object board and determines the called AIPlayer‘s scores for the columns in board."""

        scores = [50] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1

            elif board.is_win_for(self.checker):
                scores[col] = 100

            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0

            elif self.lookahead == 0:
                scores[col] = 50

            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                maxscore = max(opp_scores)

                if maxscore == 0:
                    scores[col] = 100
                if maxscore == 100:
                    scores[col] = 0
                if maxscore == 50:
                    scores[col] = 50

                board.remove_checker(col)

        return scores
                
                



    def next_move(self, board):
        """return the called AIPlayer‘s judgment of its best possible move"""
        
        self.num_moves +=1
        scores = self.scores_for(board)
        return self.max_score_column(scores)
