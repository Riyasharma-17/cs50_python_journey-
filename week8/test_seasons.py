from seasons import convert


def test_convert():
    assert convert(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert(1440) == "One thousand, four hundred forty"
    assert convert(1) == "One"