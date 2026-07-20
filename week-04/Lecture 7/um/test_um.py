import pytest
from um import count

def test_um():
    assert count("um") == 1

def test_um_blank():
    assert count(" um ") == 1

def test_um_case():
    assert count("Um") == 1

def test_um_words():
    assert count("Um yummy") == 1
