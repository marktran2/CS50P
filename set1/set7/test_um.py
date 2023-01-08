from um import count
import pytest

def test_start_um():
    assert count("um? This should...um...be...um...for a lack of a better word, clear") == 3


def test_um_greeting():
    assert count("Hello, um, I think, um uh, this is room 7...right?") == 2


def test_um_in_word():
    assert count("glum alumi's mum rums the summed gummies") == 0