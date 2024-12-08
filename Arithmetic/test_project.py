import unittest
from unittest.mock import patch, MagicMock
from project import (  
    ifAddition,
    ifSubtraction,
    ifMultiplication,
    ifDivision,
    ifModulus,
    ifMixed
)

# Mocking Pygame
import pygame
pygame.mixer = MagicMock()

class TestArithmeticGame(unittest.TestCase):

    def test_ifAddition(self):
        previous_pairs = []
        score = 0
        user_id = "test_user"
        leaderboard = {}

        with patch('builtins.input', side_effect=['5']), patch('random.randint', side_effect=[2, 3]):
            score = ifAddition(1, score, previous_pairs, user_id, leaderboard)
            self.assertEqual(score, 1)  # Expecting score to increase by 1

    def test_ifSubtraction(self):
        previous_pairs = []
        score = 0
        user_id = "test_user"
        leaderboard = {}

        with patch('builtins.input', side_effect=['1']), patch('random.randint', side_effect=[3, 2]):
            score = ifSubtraction(1, score, previous_pairs, user_id, leaderboard)
            self.assertEqual(score, 1)  # Expecting score to increase by 1

    def test_ifMultiplication(self):
        previous_pairs = []
        score = 0
        user_id = "test_user"
        leaderboard = {}

        with patch('builtins.input', side_effect=['6']), patch('random.randint', side_effect=[2, 3]):
            score = ifMultiplication(1, score, previous_pairs, user_id, leaderboard)
            self.assertEqual(score, 1)  # Expecting score to increase by 1

    def test_ifDivision(self):
        previous_pairs = []
        score = 0
        user_id = "test_user"
        leaderboard = {}

        with patch('builtins.input', side_effect=['6']), patch('random.randint', side_effect=[3, 6]):
            score = ifDivision(1, score, previous_pairs, user_id, leaderboard)
            self.assertEqual(score, 1)  # Expecting score to increase by 1

    def test_ifModulus(self):
        previous_pairs = []
        score = 0
        user_id = "test_user"
        leaderboard = {}

        with patch('builtins.input', side_effect=['1']), patch('random.randint', side_effect=[5, 2]):
            score = ifModulus(1, score, previous_pairs, user_id, leaderboard)
            self.assertEqual(score, 1)  # Expecting score to increase by 1

    def test_ifMixed(self):
        previous_pairs = []
        score = 0
        user_id = "test_user"
        leaderboard = {}

        # Mocking random.randint for numbers and random.choice for operation
        with patch('builtins.input', side_effect=['3']), \
         patch('random.randint', side_effect=[5, 2]), \
         patch('random.choice', return_value="Subtraction"):  # Mock operation to subtraction
            score = ifMixed(1, score, previous_pairs, user_id, leaderboard)
            self.assertEqual(score, 1)  # Expecting score to increase by 1

if __name__ == '__main__':
    unittest.main()
