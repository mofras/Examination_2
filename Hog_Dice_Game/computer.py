'''Module for the Computer'''
from player import Player
from random importt choice
class Computer:
    def __init__(self, difficulty):
        super().__init__("Computer")
        self.difficulty = difficulty
    
    def roll_dice(self, dice):
        if self.difficulty == "Easy":
            return dice.roll()
        elif self.difficulty == "Medium":
            return dice.roll() if choice([True, False]) else 1
        elif self.difficulty == "Hard":
            return dice.roll() if choice ([True, False]) else dice.roll()
        