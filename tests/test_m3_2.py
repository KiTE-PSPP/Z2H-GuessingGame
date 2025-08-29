import m3_2
import pytest

def test_list_third_element(capsys):
    # Phase 1: Test Case
    user_input = 3
    expected_output = "The 3rd element is 30"

    m3_2.list_third_element()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out