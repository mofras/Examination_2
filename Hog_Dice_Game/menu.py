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
            |  1. Player vs Player   |
            |  2. Player vs Computer |
            |  3. View Scoreboard    |
            |  4. View Rules         |
            |  5. Change Name        |
            |  6. Quit               |
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

    """ def change_name(self, game):
        
        print("Select the player whose name you want to change:")
        for i, player in enumerate(self.game.players, 1):
            print(f"{i}. {player.name}")

        choice = int(input("Enter the number corresponding to the player: "))
        if 1 <= choice <= len(self.game.players):
            new_name = input("Enter the new name: ")
            self.game.players[choice - 1].change_name(new_name)
            print(f"{self.game.players[choice - 1].name}'s name has been changed to {new_name}")
        else:
            print("Invalid choice. Please enter a valid number.")
        
    def get_player_names(self, players):
        '''Function to get a list of player names'''
        return [player.name for player in self.players] """