"""Module for the dice"""
import random


class Dice:
    """
    Class representing a dice object.

    This class allows for rolling a dice with a specified number of sides.
    """

    def __init__(self, num_sides=6):
        """
        Initialize a Dice object with a specified number of sides.

        Args:
            num_sides (int, optional): The number of sides on the dice.
            Defaults to 6.
        """

        self.num_sides = num_sides

    def roll(self):
        """
        Simulate rolling the dice.

        Returns:
            int: The result of rolling the dice,
            a random integer between 1 and the number of sides.
        """

        return random.randint(1, self.num_sides)
