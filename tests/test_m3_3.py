import m3_3
import pytest

def test_guessing_game_conditions_yes(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["", "yes"])   # press enter, then "yes"
    expected_output = "Number in 1 tries!"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m3_3.guessing_game_conditions()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out
    
def test_guessing_game_conditions_invalid(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["", "no"])   # press enter, then "no"
    expected_output = "I don't understand that!"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m3_3.guessing_game_conditions()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out