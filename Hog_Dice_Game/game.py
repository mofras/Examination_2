'''Module for the game'''
from dice import Dice
from player import Player
from computer import Computer
from scoreboard import Scoreboard

class Game:
    def __init__(self):
        self.players = []
        self.dice = Dice()
        self.scoreboard = Scoreboard()
        self.target_score = 20

    def add_player(self, name):
        self.players.append(Player(name))
    
    def add_computer(self, difficulty):
        self.players.append(Computer(difficulty))

    def reset_game(self):
        for player in self.players:
            player.reset_score()
        
        self.players.clear()

    def play_round(self):

        game_completed = False

        for player in self.players:
            num_dice = self.get_num_dice(player)
            roll_sum = 0
            for _ in range(num_dice):
                roll = self.dice.roll()
                print(f"{player.name} rolled: {roll}")
                if roll == 1:
                    print(f"{player.name} rolled a 1. Turn ends with o points.")
                    roll_sum = 0
                    break
                roll_sum += roll
            if roll_sum > 0: #only add if the roll_sum is greater than 0.
                print(f"{player.name}'s current score: {player.score + roll_sum}")
                player.add_score(roll_sum)
                self.scoreboard.add_score(player, roll_sum)     
            if player.score >= self.target_score:
                game_completed = True
                
        if game_completed:
            for player in self.players:
                self.scoreboard.incr_games_played(player)
        return game_completed

    def get_num_dice(self, player):
        
        while True:
            try:
                num_dice = int(input(f"{player.name}, how many dice do you want to roll? "))
                if num_dice < 1:
                    print("Please enter a positive number.")
                else:
                    return num_dice
            except ValueError:
                print("Please inter a valid number.")
    
    def display_scores(self):
        self.scoreboard.display_scores()

    def get_winner(self):
        max_score = max(player.score for player in self.players)
        winner = [player.name for player in self.players if player.score == max_score]
        return winner, max_score
