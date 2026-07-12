from twttr import shorten

def test_argument():
    assert shorten("David") == "Dvd"
    assert shorten("123") == "123"

def test_capitalisation():
    assert shorten("DAviD") == "DvD"

def test_punctuation():
    assert shorten("D.a,vid") == "D.,vd"
