import unittest
from player import Player
from dice import Dice


class TestPlayer(unittest.TestCase):

    def setUp(self):
        """Create an instance of the Player class for each test method"""
        self.player = Player("Messi")

    def test_roll_dice(self):
        """Test method to verify if roll_dice() returns a valid dice roll result"""
        dice = Dice()
        roll_result = self.player.roll_dice(dice)
        """Assert that the roll result is within the valid range
        (1 to 6 for a standard six-sided die)"""
        self.assertTrue(1 <= roll_result <= 6)

    def test_add_score(self):
        """Test method to verify if add_score() correctly
        adds points to the player's score"""
        initial_score = self.player.score
        added_points = 50
        expected_score = initial_score + added_points
        self.player.add_score(added_points)
        # Assert that the player's score matches the expected score
        self.assertEqual(self.player.score, expected_score)

    def test_reset_score(self):
        """Test method to verify if reset_score() correctly
        resets the player's score to zero"""
        self.player.score = 100
        self.player.reset_score()
        # Assert that the player's score is reset to zero
        self.assertEqual(self.player.score, 0)

    def test_change_name(self):
        """Test method to verify if change_name() correctly
        changes the player's name"""
        new_name = "Kalle"
        self.player.change_name(new_name)
        # Assert that the player's name matches the new name
        self.assertEqual(self.player.name, new_name)

    def test_roll_dice_with_custom_dice(self):
        """Test method to verify if roll_dice() returns a valid dice
        roll result with a custom dice object"""

        class CustomDice:
            def roll(self):
                return 3

        custom_dice = CustomDice()
        # Roll the custom dice
        roll_result = self.player.roll_dice(custom_dice)
        # Assert that the roll result matches the custom roll result
        self.assertEqual(roll_result, 3)


if __name__ == "__main__":
    unittest.main()
