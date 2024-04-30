from menu import Menu

'''Moddule for the main function'''

def main():
    menu = Menu()
    
    while True:
        menu.display_menu()
        choice = input("Enter a choice: ")


if __name__ == "__main__":
    main()