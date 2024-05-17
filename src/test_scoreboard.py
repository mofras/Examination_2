"""Module for testing Scoreboard class."""
import unittest
import sys
from io import StringIO
from scoreboard import Scoreboard
from player import Player


class TestScoreboard(unittest.TestCase):
    """Testing the class."""

    def setUp(self):
        """Create an instance of the Scoreboard class."""
        self.scoreboard = Scoreboard()

    def test_add_score(self):
        """Test method to verify if add_score() correctly adds
        a score to a player's total score."""
        player = Player("Test Player")
        initial_score = 0
        added_score = 50
        expected_score = initial_score + added_score
        self.scoreboard.add_score(player, added_score)
        # Assert that the player's total score matches the expected score
        self.assertEqual(self.scoreboard.scores[player.name], expected_score)

    def test_incr_games_played(self):
        """Test method to verify if incr_games_played() correctly
        increments the games played count for a player."""
        player = Player("Test Player")
        initial_games_played = 0
        expected_games_played = initial_games_played + 1
        self.scoreboard.incr_games_played(player)
        # Assert that the player's games played count matches
        # the expected count
        self.assertEqual(
            self.scoreboard.games_played[player.name], expected_games_played
        )

    def test_add_score_multiple_players(self):
        """Test method to verify if add_score() correctly
        adds scores for multiple players."""
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        self.scoreboard.add_score(player1, 100)
        self.scoreboard.add_score(player2, 150)
        # Assert that both players' scores are correctly added
        self.assertEqual(self.scoreboard.scores[player1.name], 100)
        self.assertEqual(self.scoreboard.scores[player2.name], 150)

    def test_incr_games_played_multiple_players(self):
        """Test method to verify if incr_games_played() correctly
        increments games played for multiple players."""
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        self.scoreboard.incr_games_played(player1)
        self.scoreboard.incr_games_played(player2)
        # Assert that games played are correctly incremented for both players
        self.assertEqual(self.scoreboard.games_played[player1.name], 1)
        self.assertEqual(self.scoreboard.games_played[player2.name], 1)

    def test_display_scores(self):
        """Test method to verify if display_scores()
        prints the scoreboard correctly."""
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        self.scoreboard.add_score(player1, 100)
        self.scoreboard.add_score(player2, 150)
        self.scoreboard.incr_games_played(player1)
        self.scoreboard.incr_games_played(player2)
        # Redirect stdout to a StringIO object to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Call the display_scores method
        self.scoreboard.display_scores()
        # Reset stdout to sys.__stdout__
        sys.stdout = sys.__stdout__
        # Define the expected output
        expected_output = """
--------------------------------SCOREBOARD---------------------------------
---------------------------------------------------------------------------
Player 1  : Total Score - 100, Games Played - 1, Average Score - 100.00
Player 2  : Total Score - 150, Games Played - 1, Average Score - 150.00
---------------------------------------------------------------------------
"""
        # Assert that the captured output matches the expected output
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
