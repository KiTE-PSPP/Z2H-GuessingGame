import pytest
import m1_2

def test_guessing_game_print_only(capsys):
    expected_output = "Number 3 guessed in 1 tries!"

    m1_2.guessing_game_print_only()
    captured = capsys.readouterr()

    assert expected_output in captured.out