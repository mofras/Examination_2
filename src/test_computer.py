"""Module for testing Computer class."""

import unittest
from computer import Computer
from dice import Dice


class TestComputer(unittest.TestCase):
    """Testing the class."""

    def test_roll_dice_easy(self):
        """Tests the roll range (1-6)with difficulty Easy."""
        computer = Computer("Easy")
        dice = Dice()
        rolled_value = computer.roll_dice(dice)
        self.assertGreaterEqual(rolled_value, 1)
        self.assertLessEqual(rolled_value, 6)

    def test_roll_dice_medium(self):
        """Tests the roll range (1-6) with difficulty Medium."""
        computer = Computer("Medium")
        dice = Dice()
        rolled_value = computer.roll_dice(dice)
        self.assertGreaterEqual(rolled_value, 1)
        self.assertLessEqual(rolled_value, 6)

    def test_roll_dice_hard(self):
        """Tests the roll range (1-6)with difficulty Hard."""
        computer = Computer("Hard")
        dice = Dice()
        rolled_value = computer.roll_dice(dice)
        self.assertGreaterEqual(rolled_value, 1)
        self.assertLessEqual(rolled_value, 6)

    def test_init_easy(self):
        """Tests Initialization of the Computer object with difficulty Easy."""
        computer = Computer("Easy")
        self.assertEqual(computer.name, "Computer")
        self.assertEqual(computer.difficulty, "Easy")

    def test_init_medium(self):
        """Tests Initialization of the Computer object with difficulty Medium."""
        computer = Computer("Medium")
        self.assertEqual(computer.name, "Computer")
        self.assertEqual(computer.difficulty, "Medium")

    def test_init_hard(self):
        """Tests Initialization of the Computer object with difficulty Hard."""
        computer = Computer("Hard")
        self.assertEqual(computer.name, "Computer")
        self.assertEqual(computer.difficulty, "Hard")

    def test_roll_dice_invalid_difficulty(self):
        """Tests an invalid difficulty level."""
        computer = Computer("Invalid")
        dice = Dice()
        with self.assertRaises(ValueError):
            computer.roll_dice(dice)


if __name__ == "__main__":
    unittest.main()
