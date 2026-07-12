from plates import is_valid

def test_middle_num():
    assert is_valid("AA55AA") == False

def test_start_with_alpha():
    assert is_valid("12") == False
    assert is_valid("A2") == False
    assert is_valid("2A") == False

def test_punctuation():
    assert is_valid("AA.555") == False

def test_zeros():
    assert is_valid("AAA000") == False

def test_valid():
    assert is_valid("AAA555") == True

def test_length():
    assert is_valid("AAAA5555") == False
