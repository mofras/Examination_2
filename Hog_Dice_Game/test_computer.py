import unittest
from computer import Computer
from dice import Dice
class TestComputer(unittest.TestCase):

    def test_roll_dice_easy(self):
        '''Create a Computer object with difficulty Easy'''
        computer = Computer("Easy")
        dice = Dice()
        rolled_value = computer.roll_dice(dice)
        self.assertGreaterEqual(rolled_value, 1)
        self.assertLessEqual(rolled_value, 6)

    def test_roll_dice_medium(self):
        '''Create a Computer object with difficulty Medium'''
        computer = Computer("Medium")
        dice = Dice()
        rolled_value = computer.roll_dice(dice)
        self.assertGreaterEqual(rolled_value, 1)
        self.assertLessEqual(rolled_value, 6)
        #self.assertIn(rolled_value, [1, 2, 3, 4, 5, 6])

    def test_roll_dice_hard(self):
        '''Create a Computer object with difficulty Hard'''
        computer = Computer("Hard")
        dice = Dice()
        rolled_value = computer.roll_dice(dice)
        self.assertGreaterEqual(rolled_value, 1)
        self.assertLessEqual(rolled_value, 6)

    def test_init_easy(self):
        '''Create a Computer object with difficulty Easy'''
        computer = Computer("Easy")
        self.assertEqual(computer.name, "Computer")
        self.assertEqual(computer.difficulty, "Easy")

    def test_init_medium(self):
        '''Create a Computer object with difficulty Medium'''
        computer = Computer("Medium")
        self.assertEqual(computer.name, "Computer")
        self.assertEqual(computer.difficulty, "Medium")

    def test_init_hard(self):
        '''Create a Computer object with difficulty Hard'''
        computer = Computer("Hard")
        self.assertEqual(computer.name, "Computer")
        self.assertEqual(computer.difficulty, "Hard")

    def test_roll_dice_invalid_difficulty(self):
        '''Create a Computer object with an invalid difficulty'''
        computer = Computer("Invalid")
        dice = Dice()
        with self.assertRaises(ValueError):
            computer.roll_dice(dice)



if __name__== '__main__':
    unittest.main()