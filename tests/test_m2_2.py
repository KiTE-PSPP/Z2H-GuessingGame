import m2_2
import pytest

def test_guessing_game_with_input(monkeypatch, capsys):
    # Phase 1: Test Case
    # First "" simulates pressing Enter, second "" simulates response to "Is it 3?"
    inputs = iter(["", ""])
    expected_output = "Number 3 guessed in 1 tries!"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m2_2.guessing_game_with_input()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out