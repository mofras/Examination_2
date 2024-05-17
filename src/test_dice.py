"""Module for testing Dice class."""

import unittest
from dice import Dice



class TestDice(unittest.TestCase):
    """Testing the class."""

    def test_init_default_num_sides(self):
        """Test the initialization of the Dice class
        with the default number of sides."""
        dice = Dice()
        self.assertEqual(dice.num_sides, 6)

    def test_init_custom_num_sides(self):
        """Test the initialization of the Dice class
        with a custom number of sides."""
        num_sides = 8
        dice = Dice(num_sides)
        self.assertEqual(dice.num_sides, num_sides)

    def test_roll_randomness(self):
        """Test randomness of the rolls."""
        num_sides = 6
        dice = Dice(num_sides)
        results = set()
        for _ in range(1000):
            result = dice.roll()
            results.add(result)
        # Assert that at least two different
        # results were obtained (indicating randomness)
        self.assertGreater(len(results), 1)

    def test_roll_range(self):
        """Tests results of each roll is b/n 1-6."""
        num_sides = 6
        dice = Dice(num_sides)
        for _ in range(100):
            result = dice.roll()
            # Assert that the result is within
            # the valid range of 1 to the number of sides of the dice
            self.assertTrue(1 <= result <= num_sides)


if __name__ == "__main__":
    unittest.main()
