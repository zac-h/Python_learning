import pytest
from working import convert

def test_format1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_format2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_format3():
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_format4():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"

def test_invalid1():
    with pytest.raises(ValueError):
      convert("9 AM to 13 PM")

def test_invalid2():
    with pytest.raises(ValueError):
      convert("9 AM 5 PM")
