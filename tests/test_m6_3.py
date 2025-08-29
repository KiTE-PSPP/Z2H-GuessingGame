import m6_3
import pytest

def test_binary_search_with_function(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["", "l", "yes"])  # enter, then lower, then yes
    expected_output = "Number of tries: 2"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m6_3.binary_search_with_function()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out