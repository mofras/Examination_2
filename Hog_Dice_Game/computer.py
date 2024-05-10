'''Module for the Computer'''
from player import Player
from random import choice
class Computer(Player):
    '''
    Class representing a computer player in the Dice Hog game.
    
    This class inherits from the Player class and implements AI logic for computer-controlled players.
    '''

    def __init__(self, difficulty):
        '''
        Initialize a Computer object.
        
        Args:
            difficulty (str): The difficulty level of the computer player. 
                Can be one of 'Easy', 'Medium', or 'Hard'.
        '''

        super().__init__("Computer")
        self.difficulty = difficulty
    
    def roll_dice(self, dice):
        '''
        Simulate rolling a dice based on the computer's difficulty level.
        
        Args:
            dice (Dice): The dice object used for rolling.
        
        Returns:
            int: The result of rolling the dice based on the computer's AI logic.
        '''

        if self.difficulty == "Easy":
            return dice.roll()
        elif self.difficulty == "Medium":
            return dice.roll() if choice([True, False]) else 1
        elif self.difficulty == "Hard":
            return dice.roll() if choice ([True, False]) else dice.roll()
        