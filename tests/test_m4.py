import m4_1
import pytest

def test_nested_guessing_game_first_yes(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["", "yes"])   # enter, then "yes" at first question
    expected_output = "Number 3 guessed in 1 tries!"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m4_1.nested_guessing_game()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out


def test_nested_guessing_game_second_yes(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["", "no", "yes"])   # enter, "no" for 1, "yes" for 3
    expected_output = "Number 3 guessed in 2 tries!"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m4_1.nested_guessing_game()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out


def test_nested_guessing_game_invalid(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["", "no", "maybe"])   # enter, "no" for 1, "maybe" for 3
    expected_output = "I don't understand that!"

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m4_1.nested_guessing_game()
    captured = capsys.readouterr()

    assert expected_output in captured.out