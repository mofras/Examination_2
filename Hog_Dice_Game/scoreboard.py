'''Module for the scoreboard'''
class Scoreboard:
    def __init__(self):
        self.scores = {}
    
    def add_score(self, player_name, score):
        self.scores[player_name] = score

    def display_scores(self):
        print("SCOREBOARD")
        print("-----------")
        for player, score in self.scores.items():
            print(f"{player}: {score}")