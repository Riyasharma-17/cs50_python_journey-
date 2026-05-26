# test_plates.py

from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False


def test_zero():
    assert is_valid("CS05") == False


def test_numbers_end():
    assert is_valid("AAA222") == True
    assert is_valid("AA22AA") == False


def test_punctuation():
    assert is_valid("PI3.14") == False