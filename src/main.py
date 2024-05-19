"""Moddule for the main function."""
# pylint: disable=E0401
from menu import Menu
from game import Game
from rules import Rules


def main():
    """
    Main function to run the Pig "Hog" game.

    This function initializes the game components, displays the menu, and
    handles user input to start the game, display the scoreboard, view rules,
    change player names, or quit the game.
    """
    menu = Menu()
    game = Game()
    rules = Rules()
    previous_players = []

    while True:
        print(
            """
             🎲 WELCOME TO PIG "HOG" GAME! 🎲
        """
        )
        menu.display_menu()
        choice = input("Enter a choice: ")

        if choice == "1":
            # player aginst player
            while True:
                menu.display_game_menu()
                choice = input("Choose a game: ")
                if choice == "1":
                    player1_name = input("Enter player 1 name: ")
                    player2_name = input("Enter player 2 name: ")
                    game.add_player(player1_name)
                    game.add_player(player2_name)
                    while True:
                        if game.play_round():
                            winner, max_score = game.get_winner()
                            game.announce_winner(winner, max_score)
                            game.reset_game()
                            previous_players = [player1_name, player2_name]
                            break

                elif choice == "2":
                    # Player vs Computer
                    menu.display_game_level()
                    difficulty = None
                    choice = input("Choose a level: ")
                    if choice == "1":
                        difficulty = "Easy"
                    elif choice == "2":
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
                elif choice == "3":
                    break
                else:
                    menu.print_warning("Invalid choice. Please choose 1 or 2.")
                    continue
                break
        elif choice == "2":
            game.display_scores()
        elif choice == "3":
            rules.display_rules()
        elif choice == "4":
            if previous_players:
                game.change_name(previous_players, game.scoreboard)
                # game.get_player_names(game.players)
            else:
                print("There are no players to change their name.")
        elif choice == "5":
            break
        else:
            menu.print_warning("Invalid choice. Please try again")
            continue


if __name__ == "__main__":
    main()
