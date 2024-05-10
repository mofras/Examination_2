'''Module for the scoreboard'''
class Scoreboard:
    def __init__(self):
        self.scores = {}
        self.games_played = {}
    
    def add_score(self, player, score):
        if player.name not in self.scores:
            self.scores[player.name] = 0
        self.scores[player.name] += score
    

    #self.scores.append((player.name, score))
       
      
        """ for i, (name, current_score) in enumerate(self.scores):
            if name == player.name:
                self.scores[i] = (name, current_score + score)
                break """
        

    def incr_games_played(self, player):
        if player.name not in self.games_played:
            self.games_played[player.name] = 0
        self.games_played[player.name] += 1 
    
    #def clear(self):
        #self.scores = {}
        #self.games_played = {}
      
    
    """ def increment_score(self, player, score):
        for i, (name, current_score) in enumerate(self.scores):
            if name == player.name:
                self.scores[i] = (name, current_score + score)
                break """

    def display_scores(self):
        print("--------------------------------SCOREBOARD---------------------------------")
        print("---------------------------------------------------------------------------")
        for player, score in self.scores.items():
            
            games_played = self.games_played.get(player, 0)
            #games_played = sum(1 for name in self.games_played if name == player)
            average_score = score / games_played if games_played > 0 else 0
            print(f"{player.ljust(10)}: Total Score - {score}, Games Played - {games_played}, Average Score - {average_score:.2f}")
        print("---------------------------------------------------------------------------")