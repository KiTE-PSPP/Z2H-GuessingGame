import m5_2
import pytest

def test_while_loop_with_condition_negative_then_stop(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["-1", "0"])   # first -1, then 0 to stop
    expected_outputs = ["The number is negative", "Program stopped"]

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m5_2.while_loop_condition()
    captured = capsys.readouterr()

    # Answer Validation
    for expected in expected_outputs:
        assert expected in captured.out


def test_while_loop_with_condition_positive_then_stop(monkeypatch, capsys):
    # Phase 1: Test Case
    inputs = iter(["5", "0"])   # first positive, then stop
    expected_outputs = ["The number is positive", "Program stopped"]

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    m5_2.while_loop_condition()
    captured = capsys.readouterr()

    # Answer Validation
    for expected in expected_outputs:
        assert expected in captured.out