import pytest
from fuel import convert, gauge

def test_gauge_input():
    assert gauge(25) == "25%"

def test_gauge_full():
    assert gauge(99) == "F"

def test_gauge_empty():
    assert gauge(1) == "E"

def test_convert_number():
    assert convert("1/4") == 25

def test_convert_denom_zero():
    with pytest.raises(ZeroDivisionError):
      convert("1/0")

def test_convert_denom_big():
    with pytest.raises(ValueError):
      convert("2/1")

def test_convert_negative():
    with pytest.raises(ValueError):
      convert("-1/4")

