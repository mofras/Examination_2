import unittest
import sys
from io import StringIO
from menu import Menu

class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()

    def test_display_menu(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.menu.display_menu()
        sys.stdout = sys.__stdout__
        expected_output = '''
                **************************
                |          Manu          |
                |                        |
                |  1. Start Game         |
                |  2. View Scoreboard    |
                |  3. View Rules         |
                |  4. Change Name        |
                |  5. Quit               |
                |                        |
                **************************
            '''
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())


    def test_display_game_menu(self):
            captured_output = StringIO()
            sys.stdout = captured_output
            self.menu.display_game_menu()
            sys.stdout = sys.__stdout__
            expected_output = ('''
                **************************
                |      Choose a game     |
                |                        |
                |  1. Player vs Player   |
                |  2. Player vs Computer |
                |                        |
                **************************
            ''')
            self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_display_game_level(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.menu.display_game_level()
        sys.stdout = sys.__stdout__
        expected_output = '''
                **************************
                |      Choose a level    |
                |                        |
                |  1. Easy               |
                |  2. Medium             |
                |  3. Hard               |
                |                        |
                **************************
            '''
        self.assertEqual(captured_output.getvalue().strip(), expected_output.strip())

    def test_print_warning(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.menu.print_warning("Test warning")
        sys.stdout = sys.__stdout__
        expected_output = '\033[91mTest warning\033[00m'
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_print_warning_not_called(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.menu.print_warning("")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "")

    def test_print_warning_multiple_calls(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.menu.print_warning("Test warning")
        self.menu.print_warning("Another warning")
        sys.stdout = sys.__stdout__
        expected_output = '\033[91mTest warning\033[00m\n\033[91mAnother warning\033[00m'
        self.assertEqual(captured_output.getvalue().strip(), expected_output)





if __name__ == '__main__':
    unittest.main()