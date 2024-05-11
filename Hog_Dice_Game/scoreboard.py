'''Module for the scoreboard'''
class Scoreboard:
    '''
    Class representing a scoreboard for the game.

    This class keeps track of player scores and games played.
    '''

    def __init__(self):
        '''
        Initialize the Scoreboard object.
        '''

        self.scores = {}
        self.games_played = {}
    
    def add_score(self, player, score):
        '''
        Add a score to the scoreboard for a player.

        Args:
            player (Player): The player whose score is being added.
            score (int): The score to add to the player's total score.
        '''

        if player.name not in self.scores:
            self.scores[player.name] = 0
        self.scores[player.name] += score
        
    def incr_games_played(self, player):
        '''
        Increment the number of games played for a player.

        Args:
            player (Player): The player whose games played count is being incremented.
        '''

        if player.name not in self.games_played:
            self.games_played[player.name] = 0
        self.games_played[player.name] += 1 
    
   

    def display_scores(self):
        '''
        Display the scores and statistics on the scoreboard.
        '''

        print("--------------------------------SCOREBOARD---------------------------------")
        print("---------------------------------------------------------------------------")
        for player, score in self.scores.items():
            
            games_played = self.games_played.get(player, 0)
            average_score = score / games_played if games_played > 0 else 0
            print(f"{player.ljust(10)}: Total Score - {score}, Games Played - {games_played}, Average Score - {average_score:.2f}")
        print("---------------------------------------------------------------------------")