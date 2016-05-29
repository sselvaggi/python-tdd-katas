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
        return#nothing by now
    def test_player1_wins(self):
        #0 - 0
        set = TennisSet(['player1','player2'])
        #15 - 0

        set.doScore('player1')
        #30 - 0
        set.doScore('player1')
        #40 - 0
        set.doScore('player1')
        #'player1' wins
        set.doScore('player1')
        self.assertEqual(set.state, 'finished')
        self.assertEqual(set.winner, 'player1')

    def test_player2_wins(self):
        #0 - 0
        set = TennisSet(['player1','player2'])
        #0 - 15

        set.doScore('player2')
        #0 - 30
        set.doScore('player2')
        #0 - 40
        set.doScore('player2')
        #'player2' wins
        set.doScore('player2')
        self.assertEqual(set.state, 'finished')
        self.assertEqual(set.winner, 'player2')

    def test_deuce(self):
        #0 - 0
        set = TennisSet(['player1','player2'])
        
        #0 - 15
        set.doScore('player2')
        #0 - 30
        set.doScore('player2')
        #0 - 40
        set.doScore('player2')

        #15 - 40
        set.doScore('player1')
        #30 - 40
        set.doScore('player1')
        #40 - 40 (deuce)
        set.doScore('player1')

        self.assertEqual(set.state, 'deuce')

        #'player2' get advantage
        set.doScore('player2')
        # self.assertEqual(set.state, 'finished')
        # self.assertEqual(set.winner, 'player2')


class TennisSet:
    def __init__(self, player_names):
        self.player_names = player_names
        self.score = {player_names[0]:0, player_names[1]:0}
        self.state = "playing"
        self.winner = "?"
        print self.score
    
    def otherPlayer(self,player_name):
        if(self.player_names[0]==player_name):
            return self.player_names[1]
        else:
            return self.player_names[0]

    def doScore(self,player_name):
        if(self.state == "playing"):
            if(self.score[player_name] == 0):
                self.score[player_name] = 15
            elif(self.score[player_name] == 15):
                self.score[player_name] = 30
            elif(self.score[player_name] == 30):
                self.score[player_name] = 40
                if(self.score[self.otherPlayer(player_name)] == 40):
                    self.state = "deuce"
            elif(self.score[player_name] == 40):
                if(self.score[self.otherPlayer(player_name)] < 40):
                    self.state = "finished"
                    self.winner = player_name

        
        if(self.winner != '?'):
            print player_name+" wins."
        else:
            print self.score

     
if __name__ == '__main__':
    unittest.main()