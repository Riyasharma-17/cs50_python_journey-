from um import count


def test_single_um():
    assert count("um") == 1


def test_multiple_um():
    assert count("um, thanks, um") == 2


def test_case_insensitive():
    assert count("UM") == 1


def test_not_substring():
    assert count("yummy") == 0