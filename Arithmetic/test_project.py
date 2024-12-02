import pytest
from project import (
    ifAddition,
    ifSubtraction,
    ifMultiplication,
    ifDivision,
    ifModulus,
    ifMixed,
    load_leaderboard,
    save_leaderboard,
    update_leaderboard,
    generate_unique_pair,
    display_leaderboard
)


# Test Addition Function
def test_ifAddition(monkeypatch):
    inputs = iter(["5"])  # Simulate correct input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    score = ifAddition(1, 0, [], "user1", {"user1": 0})
    assert score == 1


# Test Subtraction Function
def test_ifSubtraction(monkeypatch):
    inputs = iter(["3"])  # Simulate correct input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    score = ifSubtraction(1, 0, [(5, 2)], "user1", {"user1": 0})
    assert score == 1


# Test Multiplication Function
def test_ifMultiplication(monkeypatch):
    inputs = iter(["15"])  # Simulate correct input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    score = ifMultiplication(1, 0, [(3, 5)], "user1", {"user1": 0})
    assert score == 1


# Test Division Function
def test_ifDivision(monkeypatch):
    inputs = iter(["5"])  # Simulate correct input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    score = ifDivision(1, 0, [(10, 2)], "user1", {"user1": 0})
    assert score == 1


# Test Modulus Function
def test_ifModulus(monkeypatch):
    inputs = iter(["2"])  # Simulate correct input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    score = ifModulus(1, 0, [(5, 3)], "user1", {"user1": 0})
    assert score == 1


# Test Mixed Function
def test_ifMixed(monkeypatch):
    inputs = iter(["7"])  # Simulate correct input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    leaderboard = {"Mixed": {}}
    score = ifMixed(1, 0, [(5, 2)], "user1", leaderboard)
    assert score == 1
    assert leaderboard["Mixed"]["user1"] == 1


# Test Load Leaderboard
def test_load_leaderboard(tmp_path):
    leaderboard = {"user1": 10, "user2": 8}
    filepath = tmp_path / "test_leaderboard.csv"
    with open(filepath, "w") as file:
        file.write("user1,10\nuser2,8\n")
    loaded = load_leaderboard(filepath.stem)
    assert loaded == leaderboard


# Test Save Leaderboard
def test_save_leaderboard(tmp_path):
    leaderboard = {"user1": 10, "user2": 8}
    filepath = tmp_path / "test_leaderboard.csv"
    save_leaderboard(filepath.stem, leaderboard)
    with open(filepath, "r") as file:
        lines = file.readlines()
    assert "user1,10\n" in lines
    assert "user2,8\n" in lines


# Test Update Leaderboard
def test_update_leaderboard():
    leaderboard = {"user1": 5}
    update_leaderboard(leaderboard, "user1", 8)
    assert leaderboard["user1"] == 8
    update_leaderboard(leaderboard, "user2", 6)
    assert leaderboard["user2"] == 6


# Test Invalid Input
def test_invalid_input(monkeypatch):
    inputs = iter(["invalid", "5"])  # Simulate invalid input followed by correct input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    score = ifAddition(1, 0, [(2, 3)], "user1", {"user1": 0})
    assert score == 1


# Test Generate Unique Pair
def test_generate_unique_pair():
    previous_pairs = [(5, 3), (3, 5)]
    num1, num2 = generate_unique_pair(previous_pairs)
    assert (num1, num2) not in previous_pairs
    assert (num2, num1) not in previous_pairs


# Test Display Leaderboard
def test_display_leaderboard(capsys):
    leaderboard = {"user1": 8, "user2": 10}
    display_leaderboard(leaderboard, "Test")
    captured = capsys.readouterr()
    assert "user2: 10" in captured.out
    assert "user1: 8" in captured.out
