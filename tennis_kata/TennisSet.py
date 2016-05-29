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