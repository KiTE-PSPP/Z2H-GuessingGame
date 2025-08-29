import m6_1
import pytest

def test_binary_search_guessing_game(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["", "yes"])  # enter, yes on first guess (50)
    expected_output = "Number of tries: 1"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m6_1.binary_search_guessing_game()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out