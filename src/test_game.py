import unittest
from unittest.mock import patch
from io import StringIO
from game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_add_player(self):
        '''Test method to verify if a player is added to the game'''
        self.game.add_player("Messi")
        self.assertEqual(len(self.game.players), 1)

    def test_add_computer(self):
        '''Test method to verify if a computer player is added to the game'''
        self.game.add_computer("Easy")
        self.assertEqual(len(self.game.players), 1)

    def test_reset_game(self):
        '''Test method to verify if the game state is correctly reset'''
        self.game.add_player("Ronaldo")
        self.game.reset_game()
        self.assertEqual(len(self.game.players), 0)

    # Mocking user input of rolling one dice
    @patch('builtins.input', return_value=1)
    def test_get_num_dice_human_player(self, mock_input):
        '''Test method to verify if the number of dice is correctly
         obtained for a human player'''
        self.game.add_player("Saka")
        num_dice = self.game.get_num_dice(self.game.players[0])
        self.assertEqual(num_dice, 1)

    def test_get_num_dice_computer_player(self):
        '''Test method to verify if the number of dice is correctly
        obtained for a computer player'''
        self.game.add_computer("Easy")
        num_dice = self.game.get_num_dice(self.game.players[0])
        #Computer can roll between 1 to 6 dice
        self.assertTrue(1 <= num_dice <= 6)

    def test_get_winner(self):
        '''Test method to verify if the winner is correctly determined'''
        self.game.add_player("Ronaldo")
        self.game.players[0].score = 50
        self.game.add_player("Messi")
        self.game.players[1].score = 100
        winner, max_score = self.game.get_winner()
        self.assertEqual(winner, ["Messi"])
        self.assertEqual(max_score, 100)

    """ def test_announce_winner(self):
        '''Test method to verify if the winner is correctly announced'''
        self.game.add_player("Saliba")
        self.game.players[0].score = 100
        winner = ["Saliba"]
        max_score = 100
        expected_output = (
            "\n🎉🎉🎉 Congratulations! You won! 🎉🎉🎉\n\n"
            f"🎉🎉🎉 The winner is {winner} with a score of {max_score}! 🎉🎉🎉\n\n"
            )
        fake_out = StringIO()
        #actual_output = fake_out.getvalue().strip()
        #print("Actual output:", repr(actual_output))

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.game.announce_winner(winner, max_score)

            actual_output = fake_out.getvalue().strip()
        self.assertEqual(actual_output, expected_output) """

    """  def test_change_name(self):
        '''Test method to verify if the name change functionality works correctly'''
        self.game.add_player("Saliba")
        self.game.add_player("White")
        with patch('builtins.input', side_effect=["White", "Jesus"]):
            self.game.change_name(["Saliba", "White"], self.game.scoreboard)
        # Name remains unchanged if not selected for change
        self.assertEqual(self.game.players[0].name, "Saliba")
        self.assertEqual(self.game.players[1].name, "Jesus")
        # Verify scoreboard is updated
        self.assertEqual(self.game.scoreboard.scores.get("Jesus"), 0)
        self.assertEqual(self.game.scoreboard.games_played.get("Jesus"), 0) """

    def test_display_scores(self):
        '''Test method to verify if the scores are displayed correctly'''
        self.game.add_player("Mo")
        self.game.players[0].score = 50
        # Ensure method executes without errors
        self.game.display_scores()


if __name__ == '__main__':
    unittest.main()
