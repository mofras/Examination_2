'''Module for the game'''
from dice import Dice
from player import Player
from computer import Computer
from scoreboard import Scoreboard
from menu import Menu
import time

class Game:
    '''
    Class to manage the gameplay of the Dice Hog game.
    
    This class handles various aspects of the game, including adding players, playing rounds, determining winners, etc.
    '''

    def __init__(self):
        '''
        Initialize the Game object.
        
        Initializes the list of players, dice object, scoreboard, and target score.
        '''

        self.players = []
        self.dice = Dice()
        self.scoreboard = Scoreboard()
        self.menu = Menu()
        self.target_score = 20
        #self.game_ongoing = False


    def add_player(self, name):
        '''
        Add a player to the game.
        
        Args:
            name (str): The name of the player to be added.
        '''

        self.players.append(Player(name))
    
    def add_computer(self, difficulty):
        '''
        Add a computer player to the game.
        
        Args:
            difficulty (str): The difficulty level of the computer player.
        '''

        self.players.append(Computer(difficulty))

    def reset_game(self):
        '''
        Reset the game state.
        
        Returns:
            list: A list of previous players before resetting the game.
        '''

        previous_players = self.players.copy() #[(player.name, player.score) for player in self.players]
        self.players.clear()
        return previous_players

    def play_round(self):
        '''
        Play a round of the game.
        
        Returns:
            bool: True if the game is completed, False otherwise.
        '''

        #self.game_ongoing = True
        #while self.game_ongoing:
        game_completed = False
        for player in self.players:
            num_dice = self.get_num_dice(player)
            roll_sum = 0
            for _ in range(num_dice):
                roll = self.dice.roll()
                print(f"{player.name} rolled: {roll}")
                if roll == 1:
                    print(f"{player.name} rolled a 1. Turn ends with 0 points.")
                    roll_sum = 0
                    break
                roll_sum += roll
            if roll_sum > 1: #only add if the roll_sum is greater than 0.
                print(f"{player.name}'s current score: {player.score + roll_sum}")
                player.add_score(roll_sum)
                self.scoreboard.add_score(player, roll_sum)
                #self.scoreboard.increment_score(player, roll_sum)     
            if player.score >= self.target_score:
                game_completed = True
                
        if game_completed:
            for player in self.players:
                self.scoreboard.incr_games_played(player)
        return game_completed
        #self.game_ongoing = False
    
    def get_num_dice(self, player):
        '''
        Get the number of dice to roll for a player's turn.
        
        Args:
            player (Player): The player for whom the number of dice needs to be determined.
        
        Returns:
            int: The number of dice to roll.
        '''

        if isinstance(player, Computer):
            time.sleep(3)  # Wait for 3 seconds for dramatic effect
            num_dice = self.dice.roll()  # Generate a random number of dice for the computer
            print(f"Computer rolls {num_dice} dice.")
        else:
            # For human players, prompt for input
            while True:
                try:
                    num_dice = int(input(f"{player.name}, how many dice do you want to roll? "))
                    if num_dice < 1:
                        print("Please enter a positive number.")
                    else:
                        return num_dice
                except ValueError:
                    self.menu.print_warning("Please enter a valid number.")
        return num_dice
    
    def display_scores(self):
        '''
        Display the scores of all players.
        '''

        self.scoreboard.display_scores()

    def get_winner(self):
        '''
        Get the winner of the game.
        
        Returns:
            tuple: A tuple containing a list of winners and their score.
        '''

        max_score = max(player.score for player in self.players)
        winner = [player.name for player in self.players if player.score == max_score]
        return winner, max_score

    def announce_winner(self, winner, max_score):
        '''
        Function to output the winner
        
        Args:
            winner (list): A list of winners' names.
            max_score (int): The maximum score achieved by the winners.
        '''
        
        print()
        print('''
            🎉🎉🎉 Congratulations! You won! 🎉🎉🎉''')
        print(f'''
        🎉🎉🎉 The winner is {', '.join(winner)} with a score of {max_score}! 🎉🎉🎉''')
        print()
        

    def change_name(self, players, scoreboard):
        '''
        Function for name changing
        
        Args:
            players (list): A list of Player objects.
            scoreboard (Scoreboard): The scoreboard object.
        '''

        if players:  # Check if there are previous players
            print("Select the player whose name you want to change:")
            for i, player_name in enumerate(players, 1):
                print(f"{i}. {player_name}")
            while True:
                try:
                    choice = int(input("Enter the number corresponding to the player: "))
                    if 1 <= choice <= len(players):
                        old_name = players[choice - 1]
                        print(f"Changing name for player {old_name}")
                        new_name = input("Enter the new name: ")
                        players[choice - 1] = new_name
                        if new_name == old_name:
                            self.menu.print_warning("Name alread exist")
                        else:
                            print(f"{old_name}'s name has been changed to {new_name}")
                            for name, score in self.scoreboard.scores.items():
                                if name == old_name:
                                    self.scoreboard.scores[new_name] = score
                                    del self.scoreboard.scores[old_name]
                                    break
                            for name, games_played in self.scoreboard.games_played.items():
                                if name == old_name:
                                    self.scoreboard.games_played[new_name] = games_played
                                    del self.scoreboard.games_played[old_name]
                                    break
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    self.menu.print_warning("Invalid choice. Please enter a number.")
                    continue
                break
        else:
            print("There are no players to change their name.")
    

    def get_player_names(self, players):
        '''
        Function to get a list of player names
        
        Args:
            players (list): A list of Player objects.
        
        Returns:
            list: A list of player names.
        '''

        return [player.name for player in self.players] 