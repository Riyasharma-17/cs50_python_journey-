# test_twttr.py

from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_numbers():
    assert shorten("123") == "123"


def test_punctuation():
    assert shorten("hello!") == "hll!"


def test_mixed():
    assert shorten("What's your name?") == "Wht's yr nm?"