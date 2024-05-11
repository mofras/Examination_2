import unittest
from io import StringIO
from unittest.mock import patch
from rules import Rules


class TestRules(unittest.TestCase):

    def test_display_rules(self):
        '''Tests the output of Rules class'''
        rules = Rules()
        # Create a StringIO object to capture printed output
        captured_output = StringIO()
        expected_output = '''

        Dice 'Hog' Game:
        The objective of Dice Hog is to be the first player to reach or exceed the target score,
        typically set at 100 points.

        PLAYERS:
        Dice Hog can be played by two or more players.
        Each player takes turns rolling a standard six-sided die.

        GAME:
        Players take turns rolling the die and accumulating points based on the outcomes of their rolls.
        On a player's turn, they can choose to roll one or more dice.
        The player adds up the values of the dice they rolled and accumulates that many points for the turn.
        If a player rolls a one on any of the dice, their turn ends immediately, and they lose all points
        accumulated during that turn. It's called "hogging out."

        SCORING:
        The value of each die rolled is added to the player's turn score.
        If a player rolls a one, their turn score for that round becomes zero, and they lose their turn.
        Non-one values rolled on the dice contribute to the player's turn score.
        The turn score is added to the player's total score when the player ends their turn or "hogs out."

        WINNING:
        The game continues until at least one player reaches or exceeds the target score (usually 100 points).
        Once a player reaches or exceeds the target score at the end of their turn, the game ends.
        The player with the highest total score at the end of the game is declared the winner.

    '''

        # Redirect stdout to the captured_output object
        with unittest.mock.patch('sys.stdout', new=captured_output):
            rules.display_rules()

        # Compare the captured output with the expected output
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()