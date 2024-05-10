'''Module for the menu'''
from player import Player
from game import Game
class Menu:
    def __init__(self):
        pass

    def display_menu(self):
        '''Fuction displaying for main menu'''

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
        '''Function displaying game levels'''

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
