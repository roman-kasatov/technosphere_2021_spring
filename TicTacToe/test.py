import unittest
# from unittest.mock import patch

import tic_tac_toe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = tic_tac_toe.TicTacGame()

    def test_make_field(self):
        self.game.make_field()
        self.assertEqual(self.game.field, [[' ', ' ', ' '],
                                           [' ', ' ', ' '],
                                           [' ', ' ', ' ']])

    def test_taken_position(self):
        self.game.field = [['X', ' ', ' '],
                           [' ', 'O', ' '],
                           [' ', ' ', 'X']]
        ret = self.game.get_input('1 1')
        self.assertEqual(ret, (False, ))

    def test_out_of_field_position(self):
        self.game.field = [['X', ' ', ' '],
                           [' ', 'O', ' '],
                           [' ', ' ', 'X']]
        ret = self.game.get_input('1 3')
        self.assertEqual(ret, (False, ))

    def test_correct_position(self):
        self.game.field = [['X', ' ', ' '],
                           [' ', 'O', ' '],
                           [' ', ' ', 'X']]
        ret = self.game.get_input('2 0')
        self.assertEqual(ret, (True, 2, 0))

    def test_check_winner_x(self):
        self.game.field = [['X', ' ', 'X'],
                           [' ', 'O', 'X'],
                           [' ', ' ', 'X']]
        ret = self.game.check_winner()
        self.assertEqual(ret, 'X')

    def test_check_winner_o(self):
        self.game.field = [['X', ' ', 'O'],
                           [' ', 'O', 'X'],
                           ['O', ' ', 'X']]
        ret = self.game.check_winner()
        self.assertEqual(ret, 'O')

    def test_check_winner_draw(self):
        self.game.field = [['X', 'X', 'O'],
                           ['O', 'O', 'X'],
                           ['X', 'O', 'X']]
        ret = self.game.check_winner()
        self.assertEqual(ret, 'filled')

    def test_check_winner_none(self):
        self.game.field = [['X', ' ', ' '],
                           [' ', 'O', 'X'],
                           ['O', ' ', 'X']]
        ret = self.game.check_winner()
        self.assertEqual(ret, None)


if __name__ == '__main__':
    unittest.main(buffer=True)
