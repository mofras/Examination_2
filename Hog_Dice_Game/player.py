'''Module for the player'''
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self, dice):
        return dice.roll()
    
    def add_score(self, points):
        self.score + points
    
    def reset_score(self):
        self.score = 0