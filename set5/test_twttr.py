from twttr import shorten


def test_default():
    assert shorten("hello, world") == "hll, wrld"

def test_with_numbers():
    assert shorten("a1e2i3o4u5") == "12345"

def test_with_numbers_only():
    assert shorten("123456789") == "123456789"

def test_without_vowels():
    assert shorten("pqrstvwxyz") == "pqrstvwxyz"

def test_with_all_caps():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"

def test_mixed_caps():
    assert shorten("Hi, I'm Mark Tran!") == "H, 'm Mrk Trn!"