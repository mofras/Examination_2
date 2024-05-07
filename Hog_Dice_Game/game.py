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
        #for player in self.players:
            #player.reset_score()
        
        #self.players.clear()

        previous_players = self.players.copy() #[(player.name, player.score) for player in self.players]
        self.players.clear()
        return previous_players
        

    def play_round(self):

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

    """ def change_name(self):
        new_name = input("Would you like to enter new name(s) (y/n)? ")
        if new_name == "y":
            # Retrieve current scores before clearing players
            current_scores = {player.name: self.scoreboard.scores.get(player.name) for player in self.players}
            
            #print("Current scores:", current_scores)
            self.players.clear()  # Clear existing players
            player1_name = input("Enter name of player 1: ")
            player2_name = input("Enter name of player 2: ")
            #self.player1_name = player1_name
            #self.player2_name = player2_name
            
            self.add_player(player1_name)  # Add new players
            self.add_player(player2_name)


            # Update names in scoreboard and restore scores
            for name, score in current_scores.items():
                for player in self.players:
                    if player.name == name:
                        player.score = score 
            for player in self.players:
                player.score = current_scores.get(player.name, 0)
                self.scoreboard.add_score(player, player.score)

            self.scoreboard.scores.update({player.name: self.scoreboard.scores.pop(name) for name in current_scores})

            for player in self.players:
                #player.score = current_scores.get(player.name, 0)
                #self.scoreboard.add_score(player, player.score)
                self.scoreboard.scores = {player.name: self.scoreboard.scores.get(player.name, 0) for player in self.players}
                self.scoreboard.games_played = {player.name: self.scoreboard.games_played.get(player.name, 0) for player in self.players}
                #print(f"Player: {player.name}, Score: {player_score}, Games Played: {player_games_played}")
            
            #self.scoreboard.display_scores()  # Display updated scores
        elif new_name == "n":
            print("Names remain the same")
            print("Game Ended!")
            print("Thanks for playing") """

    """ def change_name(self):

        print("Current players:", [player.name for player in self.players])
        old_name = input("Enter the name you want to change: ")
        found = False
        for player in self.players:
            if player.name == old_name:
                found = True
                new_name = input("Enter the new name: ")
                player.change_name(new_name)
                print(f"Name changed successfully from {old_name} to {new_name}")
                self.scoreboard.increment_score(player, 0)  # Reset the score for the new name
                self.scoreboard.increment_games_played(player)  # Increment games played for the new name
                self.scoreboard.display_scores()
                break
        if not found:
            print(f"Player with name {old_name} not found.") """

    def change_name(self, players, scoreboard):
        
        print("Select the player whose name you want to change:")
        for i, player in enumerate(players, 1):
            print(f"{i}. {player.name}")

        choice = int(input("Enter the number corresponding to the player: "))
        if 1 <= choice <= len(players):
            player_to_change = players[choice - 1]
            old_name = player_to_change.name
            print(f"Changing name for player {old_name}")
            new_name = input("Enter the new name: ")
            players[choice - 1].change_name(new_name)
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