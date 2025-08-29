import m6_2
import pytest

def test_add_function(monkeypatch, capsys):
    def add(num1, num2):
        return num1 + num2

    monkeypatch.setattr("builtins.input", lambda _: "3")
    num1 = int(input("Enter Number 1"))
    num2 = int(input("Enter Number 2"))
    print("The sum is", add(num1, num2))

    captured = capsys.readouterr()
    assert "The sum is 6" in captured.out