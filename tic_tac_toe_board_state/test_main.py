import unittest
from main import main

class TestMain(unittest.TestCase):
    # Test for horizontal winner X
    def test_x_winner(self):
        result = main("x,x,x,o,x,o,o,o,x")
        self.assertEqual(result, "X-winner")

    # Test for x winner with upper and lower character case
    def test_case_difference_with_x_winner(self):
        result = main("x,,x,X,O,,X,o,o")
        self.assertEqual(result, "X-winner")

    # Test for two winners
    def test_dual_winner(self):
        result = main("x,o,o,x,o,o,x,x,o")
        self.assertEqual(result, "Error: Two winners")

    # Test for vertical winner O
    def test_vertical_o_winner(self):
        result = main("o,x,o,o,x,x,o,o,x")
        self.assertEqual(result, "O-winner")

    # Test for vertical winner X
    def test_vertical_x_winner(self):
        result = main("x,o,x,o,o,x,o,x,x")
        self.assertEqual(result, "X-winner")

    # Test for diaganol winner X
    def test_diagonal_x_winner(self):
        result = main("x,o,o,o,x,o,x,o,x")
        self.assertEqual(result, "X-winner")

    # Test for opposite diagonal winner O
    def test_opposite_diagonal_o_winner(self):
        result = main("x,x,o,x,o,x,o,o,x")
        self.assertEqual(result, "O-winner")

    # Test for invalid input
    def test_invalid_gibberish(self):
        result = main("Invalid Gibberish")
        self.assertEqual(result, "Error: Invalid input")

    # Test for invalid turns
    def test_invalid_x_zero(self):
        result = main("o,,,,o,,,,o")
        self.assertEqual(result, "Error: Invalid turn count")

    # Test for invalid turn count o greater than x
    def test_invalid_turn_count_o_greater_than_x(self):
        result = main("o,o,o,o,x,x,,,")
        self.assertEqual(result, "Error: Invalid turn count")

     # Test for invalid turn count o less than x
    def test_invalid_turn_count_o_less_than_x(self):
        result = main("o,o,o,x,x,x,x,x,")
        self.assertEqual(result, "Error: Invalid turn count")

    # Test for invalid input more than nine
    def test_invalid_input_more_than_nine(self):
        result = main("o,o,o,x,x,x,x,x,x,x,x")
        self.assertEqual(result, "Error: Invalid input")
    
    def test_invalid_player_input(self):
        result = main("x,o,x,o,x,o,x,o,z")
        self.assertEqual(result, "Error: Invalid input")

    # Test for incomplete board
    def test_incomplete_board(self):
        result = main("x,o,x,o,x,x,o,o,")
        self.assertEqual(result, "Incomplete")

    def test_tie_board(self):
        result = main("x,o,x,x,x,o,o,x,o")
        self.assertEqual(result, "Tie")
    
    def test_main_exception(self):
        with self.assertRaises(Exception):
            main()