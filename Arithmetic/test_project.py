import pytest
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

@pytest.fixture
def setup_game():
    previous_pairs = []
    score = 0
    user_id = "test_user"
    leaderboard = {}
    return previous_pairs, score, user_id, leaderboard

def test_ifAddition(setup_game):
    previous_pairs, score, user_id, leaderboard = setup_game

    with patch('builtins.input', side_effect=['5']), patch('random.randint', side_effect=[2, 3]):
        score = ifAddition(1, score, previous_pairs, user_id, leaderboard)
        assert score == 1  # Expecting score to increase by 1

def test_ifSubtraction(setup_game):
    previous_pairs, score, user_id, leaderboard = setup_game

    with patch('builtins.input', side_effect=['1']), patch('random.randint', side_effect=[3, 2]):
        score = ifSubtraction(1, score, previous_pairs, user_id, leaderboard)
        assert score == 1  # Expecting score to increase by 1

def test_ifMultiplication(setup_game):
    previous_pairs, score, user_id, leaderboard = setup_game

    with patch('builtins.input', side_effect=['6']), patch('random.randint', side_effect=[2, 3]):
        score = ifMultiplication(1, score, previous_pairs, user_id, leaderboard)
        assert score == 1  # Expecting score to increase by 1

def test_ifDivision(setup_game):
    previous_pairs, score, user_id, leaderboard = setup_game

    with patch('builtins.input', side_effect=['6']), patch('random.randint', side_effect=[3, 6]):
        score = ifDivision(1, score, previous_pairs, user_id, leaderboard)
        assert score == 1  # Expecting score to increase by 1

def test_ifModulus(setup_game):
    previous_pairs, score, user_id, leaderboard = setup_game

    with patch('builtins.input', side_effect=['1']), patch('random.randint', side_effect=[5, 2]):
        score = ifModulus(1, score, previous_pairs, user_id, leaderboard)
        assert score == 1  # Expecting score to increase by 1

def test_ifMixed(setup_game):
    previous_pairs, score, user_id, leaderboard = setup_game

    # Mocking random.randint for numbers and random.choice for operation
    with patch('builtins.input', side_effect=['3']), \
         patch('random.randint', side_effect=[5, 2]), \
         patch('random.choice', return_value="Subtraction"):  # Mock operation to subtraction
        score = ifMixed(1, score, previous_pairs, user_id, leaderboard)
        assert score == 1  # Expecting score to increase by 1

if __name__ == '__main__':
    pytest.main()