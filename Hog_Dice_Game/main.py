'''Moddule for the main function'''
from menu import Menu
from game import Game
from rules import Rules
from computer import Computer



def main():
    menu = Menu()
    game = Game()
    rules = Rules()
    previous_players = []
  
    
    while True:
        print('''
             🎲 WELCOME TO PIG "HOG" GAME! 🎲
        ''')
        menu.display_menu()
        choice = input("Enter a choice: ")

        if choice == "1":
            #player aginst player
            menu.display_game_menu()
            choice = input("Choose a game: ")
            if choice == "1":
                #if not previous_players:
                player1_name = input("Enter player 1 name: ")
                player2_name = input("Enter player 2 name: ")
                game.add_player(player1_name)
                game.add_player(player2_name)
                #else:
                   #player1_name, player2_name = previous_players
                #game.reset_game_state()
                while True:
                    if game.play_round():
                        winner, max_score = game.get_winner()
                        game.announce_winner(winner, max_score)
                        previous_players = [player1_name, player2_name]
                        break
                    #choice = input("Enter 'q' to quit or any other key to restart: ")
                    #if choice.lower() == 'q':
                        #print("Game restarted")
                            #previous_players = game.reset_game_state()
                #elif input("Enter 'q' to quit the game: ") == 'q':
                        #break
            elif choice == "2":
                menu.display_game_level()
                difficulty = None
                choice = input("Choose a level: ")
                if choice == "1":
                    difficulty = "Easy"
                elif choice =="2":
                    difficulty = "Medium"
                else:
                    difficulty = "Hard"
                player_name = input("Enter your name: ")
                game.add_player(player_name)
                game.add_computer(difficulty)
                while True:
                    if game.play_round():
                        winner, max_score = game.get_winner()
                        game.announce_winner(winner, max_score)
                        game.reset_game()
                        break
                        #choice = input("Enter 'q' to quit or any other key to restart: ")
                        #if choice.lower() == 'q':
                            #break
                    #elif input("Enter 'q' to quit the game: ") == 'q':
                        #break
        elif choice == "2":
            game.display_scores()
        elif choice == "3":
            rules.display_rules()
        elif choice == "4":
            if previous_players:  # Check if there are previous players
                #for player in previous_players:
                    #print(f"Previous player: {player.name}, Score: {player.score}")
                game.change_name(previous_players, game.scoreboard) 
                game.get_player_names(game.players)
            else:
                print("There are no players to change their name.")
        elif choice == "5":
            break
        


if __name__ == "__main__":
    main()