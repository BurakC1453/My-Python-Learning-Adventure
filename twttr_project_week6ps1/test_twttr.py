import pytest
from twttr_project_week6ps1.twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("google") == "ggl"

def test_names():
    assert shorten("Burak") == "Brk"
    assert shorten("Taha") == "Th"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("123") == "123"

def test_upper():
    assert shorten("GOOGLE") == "GGL"
    assert shorten("TWITTER") == "TWTTR"

def test_punctuation():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("What's up?") == "Wht's p?"