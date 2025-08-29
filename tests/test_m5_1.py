import m5_1
import pytest

def test_while_loop(capsys):
    count = 1
    while count <= 5:
        print("Count is:", count)
        count += 1
    m5_1.while_loop()
    captured = capsys.readouterr()
    assert "Count is: 5" in captured.out