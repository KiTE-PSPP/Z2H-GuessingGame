import m5_3
import pytest

def test_guessing_game_with_loop(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["", "no", "yes"])   # enter, first wrong, then yes at 2
    expected_output = "Number of tries: 2"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m5_3.guessing_game_with_loop()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out