'''Module for the game'''
from dice import Dice
from player import Player
from computer import Computer
from scoreboard import Scoreboard
import time

class Game:
    def __init__(self):
        self.players = []
        self.dice = Dice()
        self.scoreboard = Scoreboard()
        self.target_score = 20
        #self.game_ongoing = False

    def add_player(self, name):
        self.players.append(Player(name))
    
    def add_computer(self, difficulty):
        self.players.append(Computer(difficulty))

    def reset_game(self):
        previous_players = self.players.copy() #[(player.name, player.score) for player in self.players]
        self.players.clear()
        return previous_players

    def play_round(self):
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
            if roll_sum > 0: #only add if the roll_sum is greater than 0.
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
                    print("Please enter a valid number.")
        return num_dice
    

    def display_scores(self):
        self.scoreboard.display_scores()


    def get_winner(self):
        max_score = max(player.score for player in self.players)
        winner = [player.name for player in self.players if player.score == max_score]
        return winner, max_score


    def announce_winner(self, winner, max_score):
        '''Fuction to output the winner'''
        print()
        print('''
            🎉🎉🎉 Congratulations! You won! 🎉🎉🎉''')
        print(f'''
        🎉🎉🎉 The winner is {', '.join(winner)} with a score of {max_score}! 🎉🎉🎉''')
        print()
        

    def change_name(self, players, scoreboard):
        '''Function for name changing'''
        
        print("Select the player whose name you want to change:")
        for i, player in enumerate(self.players, 1):
            print(f"{i}. {player.name}")

        choice = int(input("Enter the number corresponding to the player: "))
        if 1 <= choice <= len(self.players):
            player_to_change = self.players[choice - 1]
            old_name = player_to_change.name
            print(f"Changing name for player {old_name}")
            new_name = input("Enter the new name: ")
            self.players[choice - 1].change_name(new_name)
            print(f"{old_name}'s name has been changed to {new_name}")

            for name, score in scoreboard.scores.items():
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
    

    def get_player_names(self, players):
        '''Function to get a list of player names'''
        return [player.name for player in self.players] 