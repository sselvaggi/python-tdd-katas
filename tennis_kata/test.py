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

    def test_deuce_player1_advantage_and_deuce(self):
        self.set.score_by('player2') # 0 - 15
        self.set.score_by('player2') # 0 - 30
        self.set.score_by('player2') # 0 - 40

        self.set.score_by('player1') # 15 - 40
        self.set.score_by('player1') # 30 - 40
        self.set.score_by('player1') # 40 - 40 (deuce)

        self.assertEqual(self.set.state, 'deuce')

        #'player1' get advantage
        self.set.score_by('player1')
        self.assertEqual(self.set.state, 'advantage')
        self.assertEqual(self.set.advantage, 'player1')

        #'player2' get deuce back
        self.set.score_by('player2')
        self.assertEqual(self.set.state, 'deuce')
        
    def test_deuce_player1_advantage_and_wins(self):
        self.set.score_by('player2') # 0 - 15
        self.set.score_by('player2') # 0 - 30
        self.set.score_by('player2') # 0 - 40

        self.set.score_by('player1') # 15 - 40
        self.set.score_by('player1') # 30 - 40
        self.set.score_by('player1') # 40 - 40 (deuce)

        self.assertEqual(self.set.state, 'deuce')

        #'player1' get advantage
        self.set.score_by('player1')
        self.assertEqual(self.set.state, 'advantage')
        self.assertEqual(self.set.advantage, 'player1')

        #'player1' wins
        self.set.score_by('player1')
        self.assertEqual(self.set.state, 'finished')
        self.assertEqual(self.set.winner, 'player1')



class TennisSet:
    def __init__(self, player_names):
        self.player_names = player_names
        self.score = {player_names[0]:0, player_names[1]:0}
        self.state = "playing"
        self.winner = "?"
        print self.score
    
    def other_player(self,player_name):
        if(self.player_names[0]==player_name):
            return self.player_names[1]
        else:
            return self.player_names[0]

    def score_by(self,player_name):
        if(self.state == "playing"):
            if(self.score[player_name] == 0):
                self.score[player_name] = 15
            elif(self.score[player_name] == 15):
                self.score[player_name] = 30
            elif(self.score[player_name] == 30):
                self.score[player_name] = 40
                if(self.score[self.other_player(player_name)] == 40):
                    self.state = "deuce"
            elif(self.score[player_name] == 40):
                if(self.score[self.other_player(player_name)] < 40):
                    self.set_winner(player_name)
        elif(self.state == "deuce"):
            self.set_advantage(player_name)        
        elif(self.state == "advantage"):
            if(self.advantage == player_name):
                self.set_winner(player_name)
            else:
                self.state = "deuce"

        if(self.winner != '?'):
            print player_name+" wins."
        else:
            print self.score

    def set_advantage(self, player_name):
        self.advantage = player_name
        self.state = "advantage" 

    def set_winner(self, player_name):
        self.state = "finished"
        self.winner = player_name

if __name__ == '__main__':
    unittest.main()