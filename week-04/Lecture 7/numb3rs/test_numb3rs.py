from numb3rs import validate

def test_valid():
    assert validate("1.2.3.4") == True

def test_invalid():
    assert validate("1.2.3.277") == False
