"""Module for testing Game class."""
# pylint: disable=E0401
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from game import Game
from player import Player


class TestGame(unittest.TestCase):
    """Testing the class."""

    def setUp(self):
        """Create an instance of the Rules class."""
        self.game = Game()
        self.game.menu = MagicMock()

    def test_add_player(self):
        """
        Test method to verify if a player
        is added to the game.
        """
        self.game.add_player("Messi")
        self.assertEqual(len(self.game.players), 1)

    def test_add_computer(self):
        """
        Test method to verify if a computer
        player is added to the game.
        """
        self.game.add_computer("Easy")
        self.assertEqual(len(self.game.players), 1)

    def test_reset_game(self):
        """
        Test method to verify if the game state
        is correctly reset.
        """
        self.game.add_player("Ronaldo")
        self.game.reset_game()
        self.assertEqual(len(self.game.players), 0)

    def test_play_round(self):
        """Test method for play round."""
        player1 = Player("Alice")
        player2 = Player("Bob")
        self.game.add_player(player1)
        self.game.add_player(player2)

    # Mocking user input of rolling one dice
    @patch("builtins.input", return_value=1)
    def test_get_num_dice_human_player(self, mock_input):
        """Test method to verify if the number of dice is correctly
        obtained for a human player."""

        self.game.add_player("Saka")
        num_dice = self.game.get_num_dice(self.game.players[0])
        self.assertEqual(num_dice, 1)

    def test_get_num_dice_computer_player(self):
        """Test method to verify if the number of dice is correctly
        obtained for a computer player."""
        self.game.add_computer("Easy")
        num_dice = self.game.get_num_dice(self.game.players[0])
        # Computer can roll between 1 to 6 dice
        self.assertTrue(1 <= num_dice <= 6)

    def test_get_winner(self):
        """Test method to verify if the winner is correctly determined."""
        self.game.add_player("Ronaldo")
        self.game.players[0].score = 50
        self.game.add_player("Messi")
        self.game.players[1].score = 100
        winner, max_score = self.game.get_winner()
        self.assertEqual(winner, ["Messi"])
        self.assertEqual(max_score, 100)

    @patch("sys.stdout", new_callable=StringIO)
    def test_announce_winner_winner(self, mock_stdout):
        """Test method for winner."""
        winner = ["Player1"]
        max_score = 100
        self.game.announce_winner(winner, max_score)

        expected_output = (
            "\n"
            "\n            🎉🎉🎉 Congratulations! You won! 🎉🎉🎉\n"
            "\n        🎉🎉🎉 The winner is Player1 with a score of 100! 🎉🎉🎉\n"
            "\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("builtins.input", side_effect=["1", "NewName"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_change_name(self, mock_stdout, mock_input):
        """Test method for changin name."""
        self.game.players = ["Player1"]
        self.game.scoreboard.scores = {"Player1": 10}
        self.game.scoreboard.games_played = {"Player1": 5}
        self.game.change_name(self.game.players, self.game.scoreboard)

        expected_output = (
            "Select the player whose name you want to change:\n"
            "1. Player1\n"
            "Changing name for player Player1\n"
            "Player1's name has been changed to NewName\n"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())
        self.assertIn("NewName", self.game.players)
        self.assertIn("NewName", self.game.scoreboard.scores)
        self.assertIn("NewName", self.game.scoreboard.games_played)
        self.assertNotIn("Player1", self.game.players)
        self.assertNotIn("Player1", self.game.scoreboard.scores)
        self.assertNotIn("Player1", self.game.scoreboard.games_played)

    @patch("builtins.input", side_effect=["2", "NewName", "1", "NewName"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_change_name_invalid_choice(self, mock_stdout, mock_input):
        """Test method for changing name(invalid choice)."""
        self.game.players = ["Player1"]
        self.game.scoreboard.scores = {"Player1": 10}
        self.game.scoreboard.games_played = {"Player1": 5}

        self.game.change_name(self.game.players, self.game.scoreboard)

        expected_output = (
            "Select the player whose name you want to change:\n"
            "1. Player1\n"
            "Invalid choice. Please enter a valid number.\n"
            "Changing name for player Player1\n"
            "Player1's name has been changed to NewName\n"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["1", "Player1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_change_name_duplicate_name(self, mock_stdout, mock_input):
        """Test method for changing to similar name."""
        self.game.players = ["Player1"]
        self.game.scoreboard.scores = {"Player1": 10}
        self.game.scoreboard.games_played = {"Player1": 5}

        self.game.change_name(self.game.players, self.game.scoreboard)

        expected_output = (
            "Select the player whose name you want to change:\n"
            "1. Player1\n"
            "Changing name for player Player1\n"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())
        self.game.menu.print_warning.assert_called_with("Name alread exist")

    def test_display_scores(self):
        """Test method to verify if the scores are displayed correctly."""
        self.game.add_player("Mo")
        self.game.players[0].score = 50
        # Ensure method executes without errors
        self.game.display_scores()

    def tearDown(self):
        del self.game


if __name__ == "__main__":
    unittest.main()
