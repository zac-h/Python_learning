from bank import value

def test_hello():
    assert value("hello") == 0

def test_starts_with_h():
    assert value("hi") == 20

def test_no_hello():
    assert value("gday") == 100

def test_numbers():
    assert value("123") == 100

def test_case_sensitivity():
    assert value("HeLLo") == 0
