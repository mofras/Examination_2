"""Module for the rules"""


class Rules:
    """
    Class to define the rules of the Dice Hog game.

    This class provides a method to display the rules of the game.
    """

    def __init__(self):
        pass

    def display_rules(self):
        """
        Method to display the rules of the Dice 'Hog' game.

        This method prints out the rules of the game,
        including the objective, players,
        gameplay, scoring, and winning conditions.
        """

        print(
            """

        Dice 'Hog' Game:
        The objective of Dice Hog is to be the first player
        to reach or exceed the target score, typically set at 100 points.

        PLAYERS:
        Dice Hog can be played by two or more players.
        Each player takes turns rolling a standard six-sided die.

        GAME:
        Players take turns rolling the die and accumulating points
        based on the outcomes of their rolls. On a player's turn,
        they can choose to roll one or more dice.

        The player adds up the values of the dice they rolled
        and accumulates that many points for the turn.

        If a player rolls a one on any of the dice, their turn ends
        immediately, and they lose all points accumulated during that turn.
        It's called "hogging out."

        SCORING:
        The value of each die rolled is added to the player's turn score.
        If a player rolls a one, their turn score for that round becomes zero,
        and they lose their turn.

        Non-one values rolled on the dice contribute to the player's
        turn score.

        The turn score is added to the player's total score when
        the player ends their turn or "hogs out."

        WINNING:
        The game continues until at least one player reaches or exceeds
        the target score.

        Once a player reaches or exceeds the target score at the end
        of their turn, the game ends.

        The player with the highest total score at the end of the game
        is declared the winner.

    """
        )
