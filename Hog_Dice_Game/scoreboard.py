'''Module for the scoreboard'''
class Scoreboard:
    def __init__(self):
        self.scores = {}
        self.games_played = {}
    
    def add_score(self, player_name, score):
        if player_name not in self.scores:
            self.scores[player_name] = 0
        self.scores[player_name] += score
        

    def incr_games_played(self, player_name):
        if player_name not in self.games_played:
            self.games_played[player_name] = 0
        self.games_played[player_name] += 1


    def display_scores(self):
        print("--------------------------------SCOREBOARD---------------------------------")
        print("---------------------------------------------------------------------------")
        for player, score in self.scores.items():
            games_played = self.games_played.get(player, 0)
            average_score = score / games_played if games_played > 0 else 0
            print(f"{player.ljust(10)}: Total Score - {score}, Games Played - {games_played}, Avarage Score - {average_score}")