from working import convert
import pytest


def test_regular():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_midnight():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")