#A kata
#To try all these tools on the field, I executed the tennis kata. 
#It consists of implementing the scoring rules of a tennis set:

#Each player can have either of these points in one game, 
#described as 0-15-30-40. Each time a player scores, 
#it advances of one position in the scale.
#A player at 40 who scores wins the set. Unless...
#If both players are at 40, we are in a *deuce*. 
#If the game is in deuce, the next scoring player will gain an *advantage*. 
#Then if the player in advantage scores he wins, 
#while if the player not in advantage scores they are back at deuce.
import unittest
from TennisSet import TennisSet


class TestTennisSet(unittest.TestCase):
    def setUp(self):
        self.set = TennisSet(['player1','player2']) # 0 - 0

    def test_player1_wins(self):
        self.set.score_by('player1') # 15 - 0
        self.set.score_by('player1') # 30 - 0
        self.set.score_by('player1') # 40 - 0
        self.set.score_by('player1') # 'player1' wins
        self.assertEqual(self.set.state, 'finished')
        self.assertEqual(self.set.winner, 'player1')

    def test_player2_wins(self):
        self.set.score_by('player2') # 0 - 15
        self.set.score_by('player2') # 0 - 30
        self.set.score_by('player2') # 0 - 40
        self.set.score_by('player2') # 'player2' wins
        self.assertEqual(self.set.state, 'finished')
        self.assertEqual(self.set.winner, 'player2')

    def test_deuce(self):
        self.set.score_by('player2') # 0 - 15
        self.set.score_by('player2') # 0 - 30
        self.set.score_by('player2') # 0 - 40

        self.set.score_by('player1') # 15 - 40
        self.set.score_by('player1') # 30 - 40
        self.set.score_by('player1') # 40 - 40 (deuce)

        self.assertEqual(self.set.state, 'deuce')

    def test_deuce_and_advantage_by_player(self, player_name = "player1"):
        self.test_deuce()
        self.set.score_by(player_name) # player_name gets advantage
        self.assertEqual(self.set.state, 'advantage')
        self.assertEqual(self.set.advantage, player_name)

    def test_deuce_and_advantage_by_player1_and_deuce_back(self):
        self.test_deuce_and_advantage_by_player('player1')
        self.set.score_by('player2') # 'player2' gets deuce back
        self.assertEqual(self.set.state, 'deuce')
        
    def test_deuce_and_advantage_by_player1_and_wins(self):
        self.test_deuce_and_advantage_by_player('player1')
        self.set.score_by('player1') # 'player1' wins
        self.assertEqual(self.set.state, 'finished')
        self.assertEqual(self.set.winner, 'player1')

if __name__ == '__main__':
    unittest.main()