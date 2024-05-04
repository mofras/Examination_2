'''Moddule for the main function'''
from menu import Menu
from game import Game
from rules import Rules
from computer import Computer


def main():
    menu = Menu()
    game = Game()
    rules = Rules()

    
    while True:
        menu.display_menu()
        choice = input("Enter a choice: ")

        if choice == "1":
            #player aginst player
            player1_name = input("Enter player 1 name: ")
            player2_name = input("Enter player 2 name: ")
            game.add_player(player1_name)
            game.add_player(player2_name)
            #print(player1_name)
            #print(player2_name)
            while True:
                if game.play_round():
                    winner, max_score = game.get_winner()
                    print(f"The winner is {', ' .join(winner)} with a score of {max_score}")
                    break
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
                    print(f"The winner is {', ' .join(winner)} with a score of {max_score}")
                    break
        elif choice == "3":
            game.display_scores()
        elif choice == "4":
            rules.display_rules()
        elif choice == "5":
            break


if __name__ == "__main__":
    main()