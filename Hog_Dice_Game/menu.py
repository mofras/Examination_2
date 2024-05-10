'''Module for the menu'''
from player import Player
from game import Game
class Menu:
    '''
    Class representing a menu for the game.

    This class provides methods to display different menus in the game.
    '''
    def __init__(self):
        pass

    def display_menu(self):
        '''
        Display the main menu of the game.
        '''

        print('''
                **************************
                |          Manu          |
                |                        |
                |  1. Start Game         |
                |  2. View Scoreboard    |
                |  3. View Rules         |
                |  4. Change Name        |
                |  5. Quit               |
                |                        |
                **************************
            ''')
    
    def display_game_menu(self):
        '''
        Display the menu for choosing a game mode.
        '''

        print('''
                **************************
                |      Choose a game     |
                |                        |
                |  1. Player vs Player   |
                |  2. Player vs Computer |
                |                        |
                **************************
            ''')

    def display_game_level(self):
        '''
        Display the menu for choosing the difficulty level of the game.
        '''

        print('''
                **************************
                |      Choose a level    |
                |                        |
                |  1. Easy               |
                |  2. Medium             |
                |  3. Hard               |
                |                        |
                **************************
            ''')
