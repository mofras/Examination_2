from menu import Menu
from game import Game

'''Moddule for the main function'''

def main():
    menu = Menu()
    game = Game()

    
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
            game.play_round()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass


if __name__ == "__main__":
    main()