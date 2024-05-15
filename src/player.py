"""Module for the player"""


class Player:
    """'
    Class representing a player in the Dice Hog game.

    This class manages player attributes such as name and
    score, as well as methods for rolling dice,
    adding scores, resetting scores, and changing names.
    """

    def __init__(self, name):
        """
        Initialize a Player object.

        Args:
            name (str): The name of the player.
        """

        self.name = name
        self.score = 0

    def roll_dice(self, dice):
        """
        Simulate rolling a dice.

        Args:
            dice (Dice): The dice object used for rolling.

        Returns:
            int: The result of rolling the dice.
        """

        return dice.roll()

    def add_score(self, points):
        """
        Add points to the player's score.

        Args:
            points (int): The points to be added to the player's score.
        """

        self.score += points

    def reset_score(self):
        """Reset the player's score to zero."""

        self.score = 0

    def change_name(self, new_name):
        """
        Change the player's name.

        Args:
            new_name (str): The new name for the player.
        """

        self.name = new_name
